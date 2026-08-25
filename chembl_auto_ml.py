from chembl_webresource_client.new_client import new_client
import pandas as pd
import numpy as np
from supervised import AutoML
from sklearn.model_selection import train_test_split
from rdkit import Chem
from rdkit.Chem import SaltRemover, AllChem
import os
import streamlit as st


@st.cache_data(show_spinner=False)
def retrieve_dataset_from_chembl(chembl_id: str):
    target = new_client.target
    activity = new_client.activity

    activities = activity.filter(
        target_chembl_id=chembl_id).filter(
        standard_type__in=["IC50", "Ki"]).only(
        ['standard_value', 'molecule_chembl_id', 'type', 'pref_name']
    )
    cols = {'molecule_chembl_id':[], 'standard_value':[], 'type':[]}
    cols['molecule_chembl_id'] = [elem['molecule_chembl_id'] for elem in activities]
    cols['standard_value'] = [elem['standard_value'] for elem in activities]
    cols['type'] = [elem['type'] for elem in activities]

    df = pd.DataFrame(cols)
    df = df.dropna(axis=0)
    df["standard_value"] = df["standard_value"].astype("float")
    df["standard_value"] = np.where(df["type"] == "IC50", df["standard_value"] * 0.5, df["standard_value"])
    df["type"] = "Ki"

    molecule = new_client.molecule
    mols = molecule.filter(
        molecule_chembl_id__in=df["molecule_chembl_id"].to_list()).only(["molecule_chembl_id", "molecule_structures"])

    smiles_map = {
        cpd["molecule_chembl_id"]: (
            cpd["molecule_structures"]["canonical_smiles"]
            if cpd.get("molecule_structures")
            and cpd["molecule_structures"].get("canonical_smiles")
            else None
        )
        for cpd in mols
    }

    df2 = pd.DataFrame(data=smiles_map.items(), columns=["molecule_chembl_id", "smiles"])
    df2 = df2.dropna(subset=["molecule_chembl_id"])
    df_merged = df.merge(df2, on="molecule_chembl_id", how="left")
    df_final = df_merged.groupby("smiles", as_index=False).aggregate({"standard_value": "mean"})
    df_final["Bin_Act"] = np.where(df_final["standard_value"] <= 100, 1, 0)

    return df_final

@st.cache_data(show_spinner=False)
def chemicalize_and_prep_dataset(dataframe, test_size, random_state, radius, fpSize):
    remover = SaltRemover.SaltRemover()
    morgan_generator = AllChem.GetMorganGenerator(radius=radius, fpSize=fpSize)

    dataframe['mol'] = dataframe['smiles'].apply(lambda mol: Chem.MolFromSmiles(mol))
    dataframe['mol'] = dataframe['mol'].apply(lambda mol: remover.StripMol(mol))
    dataframe['fps'] = dataframe['mol'].apply(lambda mol: morgan_generator.GetFingerprintAsNumPy(mol))

    X = np.stack(dataframe["fps"].values)
    y = dataframe['Bin_Act']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, test_size=test_size)

    return X_train, X_test, y_train, y_test

@st.cache_resource(show_spinner=False)
def auto_ml(X_train,
            y_train,
            X_test,
            y_test,
            chembl_id,
            model_time_limit,
            results_path,
            algorithms,
            train_ensemble,
            stack_models,
            golden_features,
            features_selection,
            random_state,
            explain_level,
            mode,
            random_seed,
            eval_metric,
            radius,
            fpSize,
            folds,
            n_jobs):
    cwd_path = os.getcwd()
    results_path = os.path.join(cwd_path, f'{chembl_id}_radius{radius}_fpSize{fpSize}_ml_model')
    st.write(f'Results will be storage in {results_path}')

    os.makedirs(results_path, exist_ok=True)
    automl = AutoML(
        model_time_limit=model_time_limit,
        results_path=results_path,
        algorithms=algorithms,
        train_ensemble=train_ensemble,
        stack_models=stack_models,
        ml_task='binary_classification',
        golden_features=golden_features,
        features_selection=features_selection,
        random_state=random_state,
        explain_level=explain_level,
        eval_metric=eval_metric,
        mode=mode,
        validation_strategy={
            "validation_type": "kfold",
            "stratify": True,
            "k_folds": folds,
            "shuffle": True,
            "random_seed": random_seed,
        },
        n_jobs=n_jobs
    )

    automl.fit(X_train, y_train)
    test_score = automl.score(X_test, y_test)
    X = np.concatenate([X_train, X_test], axis=0)
    print('=======================================================================================================================================')
    print(X.shape)
    y = np.concatenate([y_train, y_test], axis=0)
    print('=======================================================================================================================================')

    print(y.shape)
    automl.need_retrain(X, y)

    return automl, test_score, results_path
