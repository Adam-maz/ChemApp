import streamlit as st
import pandas as pd
import numpy as np
import os
from joblib import load
from shutil import rmtree
from supervised import AutoML
from mol_format_converter import *
from docking_utlis import *

from ChemBERTaLM_module import combinatorial_synthesis
import torch
from chembl_auto_ml import *

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.rdMolDescriptors import (
    CalcExactMolWt,
    CalcTPSA,
    CalcFractionCSP3,
    CalcNumRotatableBonds,
    CalcNumHBA,
    CalcNumHBD,
    CalcNumAtomStereoCenters,
    CalcNumAromaticRings,
    CalcNumAliphaticRings,
)

from rdkit.Chem.QED import default
from rdkit.Chem.Crippen import MolLogP


st.set_page_config(layout="wide", page_title="ChemApp", page_icon="🧪")
st.header("ChemApp", divider="green")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


@st.cache_data
def load_data(file, radius, fpSize):
    df = pd.read_csv(file)
    df["mol"] = [Chem.MolFromSmiles(smiles) for smiles in df["smiles"]]
    df = df[df["mol"].notnull()].copy()
    morgan_generator = AllChem.GetMorganGenerator(radius=radius, fpSize=fpSize)
    df["fps"] = [morgan_generator.GetFingerprintAsNumPy(mol) for mol in df["mol"]]
    X = np.stack(df["fps"].values)
    return df, X


@st.cache_resource
def load_model(target: str):
    classifier = [file for file in os.listdir(os.getcwd()) if file.startswith(target)][0]
    model = load(classifier)
    return model

def run_lm(smiles, iterations, temperature, max_new_tokens, do_sample, top_p, top_k, num_return_sequences, repetition_penalty, num_beams):
    l1, l2 = combinatorial_synthesis(smiles=smiles, iterations=iterations, temperature=temperature, max_new_tokens=max_new_tokens,
                                     do_sample=do_sample, top_p=top_p, top_k=top_k, num_beams=num_beams, repetition_penalty=repetition_penalty,
                                     num_return_sequences=num_return_sequences)

    list_of_ids_lm = [f'cpd{id}' for id in range(len(l2))]
    dict_lm = {'id': list_of_ids_lm, 'smiles': l2, 'mols': l1}
    df_lm = pd.DataFrame(dict_lm)

    return df_lm


@st.cache_data(show_spinner=False)
def calculate_descriptors(df):

    descriptors = {
        "QED": default,
        "Molecular Weight": CalcExactMolWt,
        "LogP": MolLogP,
        "FCsp3": CalcFractionCSP3,
        "TPSA": CalcTPSA,
        "NumRotatableBonds": CalcNumRotatableBonds,
        "HBA": CalcNumHBA,
        "HBD": CalcNumHBD,
        "NumAliphaticRings": CalcNumAliphaticRings,
        "NumAromaticRings": CalcNumAromaticRings,
        "NumAtomStereoCenters": CalcNumAtomStereoCenters,
    }

    result = df.copy()

    for name, func in descriptors.items():
        result[name] = result["mol"].apply(func)

    return result


sbar = st.sidebar.radio(
    "Navigation", ["Home", "AutoML", "Data Uploading", "QSAR prediction",  "Molecular Descriptors", 'Docking', 'Visual inspection']
)

if sbar == "Home":
    st.markdown(
        """
        ChemApp is a computational platform designed to support early-stage drug discovery. The application
        integrates data collection for machine learning, automated machine learning, *de novo* molecular generation, drug-likeness
        assessment, molecular docking and docking results visualization into a unified workflow for the analysis and prioritization 
        of potentially bioactive compounds.
        """
    )
    st.text("")
    st.text("")
    st.text("")
    st.subheader("ChemApp utilities", divider="blue")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text("")
        st.badge("Retrieve Dataset, train ML-model", icon=":material/smart_toy:", color="blue")
        st.markdown(
            """Colect Dataset for particular biotarget deposited in [ChEMBL](https://www.ebi.ac.uk/chembl/) and train classifier model using [AutoML](https://supervised.mljar.com/)"""
        )

    with col2:
        st.text("")
        st.badge("Choose Your Data", icon=":material/science:", color="green")
        st.markdown(
            """Select source of your data:
- paste single SMILES string                  
- load CSV file with multiple SMILES strings
- generate molecules using [ChemBertaLM model](https://huggingface.co/gokceuludogan/ChemBERTaLM)"""
        )

    with col3:
        st.text("")
        st.badge("Predict Bioactivity", icon=":material/biotech:", color="violet")
        st.markdown(
            """Select desired molecular target and predict whether proposed ligands can iteract with it.
            Model returns binary labels:
- `1` means ligand poses bioactivity >= than 7 pKi
- `0` means ligand poses bioactivity <= than 7 pKi
"""
        )

    with col4:
        st.text("")
        st.badge("Calculate Molecular Descriptors", icon=":material/analytics:", color="orange")
        st.markdown(
            """Compute desired Molecular Descriptors derived from [RDKit](https://www.rdkit.org/docs/) and filter dataset to obtain only druglikeable molecules"""
        )

    with col5:
        st.text("")
        st.badge("Perform Molecular Docking", icon=":material/genetics:", color="red")
        st.markdown(
            """Dock desired molecules into target's active site with the use of [AutoDock Vina](https://autodock-vina.readthedocs.io/en/latest/docking_python.html)
             and inspect resulted poses interactively"""
        )


elif sbar == "AutoML":

    st.write("")
    st.write("")
    st.write("")

    col6, col7, col8 = st.columns(3)


    with col6:
        retrieve_status = st.empty()
        st.badge("Retrieving Dataset From ChEMBL",icon=":material/science:")
        chembl_id = st.text_input("Enter ChEMBL ID for desired biological target")
        retrieve_button = st.button("Retrieve dataset")

    with col7:
        chemicalize_status = st.empty()
        st.badge("Dataset Chemicalization and Splitting",icon=":material/biotech:", color="green")

        radius = st.number_input("Choose radius", min_value=1, max_value=4, value=3)
        fpSize = st.selectbox("Choose fingerprint size", options=[pow(2, i) for i in range(10, 14)])
        split_random_state = st.number_input("Choose random seed for dataset split", value=42)
        test_size = st.number_input("Choose test size", min_value=0.1, max_value=1.0, value=0.3)
        chemicalize_button = st.button("Chemicalize and split dataset")

    with col8:
        train_status = st.empty()
        st.badge("AutoML", icon=":material/smart_toy:", color="violet")
        model_time_limit = st.number_input("Choose model time limit (seconds)", min_value=1, value=3600)
        results_path = st.text_input("Results path", value="automl_results")
        algorithms = st.multiselect(
            "Algorithms",
            options=[
                "Random Forest",
                "Extra Trees",
                "LightGBM",
                "Xgboost",
                "CatBoost",
                "Neural Network",
            ],
            default=[
                "Random Forest",
                "LightGBM",
                "Xgboost",
                "CatBoost",
            ],
        )

        train_ensemble = st.checkbox("Train Ensemble",value=True)
        stack_models = st.checkbox("Stack Models", value=True)
        golden_features = st.checkbox("Golden Features", value=False)
        features_selection = st.checkbox("Feature Selection", value=False)
        automl_random_state = st.number_input("Random State (model)", min_value=0, value=42)
        random_seed = st.number_input("Random Seed (KFold )", min_value=0, value=42)
        folds = st.number_input("Number of folds", min_value=1, value=5)
        explain_level = st.selectbox("Explain Level", options=[0, 1, 2], index=0)
        mode = st.selectbox("AutoML Mode", options=["Explain", "Perform", "Compete", "Optuna"], index=2)
        eval_metric = st.selectbox('Evaluation Metric', options=['logloss', 'auc', 'f1', 'average_precision', 'accuracy'])
        n_jobs = st.number_input('Number of jobs', min_value=-1, max_value=os.cpu_count() ,value=-1)
        train_button = st.button("Train Model")


    if retrieve_button:
        if not chembl_id:
            retrieve_status.warning("Provide ChEMBL ID")
        else:
            with retrieve_status:
                with st.spinner("Retrieving dataset..."):
                    chembl_data = retrieve_dataset_from_chembl(chembl_id)
                    counts = chembl_data['Bin_Act'].value_counts()

            st.session_state["chembl_data"] = chembl_data
            retrieve_status.success(f"Dataset retrieved ({len(chembl_data)} compounds)")
        with col6:
            st.divider()
            st.markdown(f'Ratio between active (**1**) and inactive (**0**) classes in preprocessed {chembl_id} dataset.')
            st.bar_chart(counts, x_label="Activity Labels ", y_label="Count", horizontal=True, color="violet")


    if chemicalize_button:
        if "chembl_data" not in st.session_state:
            chemicalize_status.warning("First retrieve dataset")
        else:
            with chemicalize_status:
                with st.spinner("Dataset chemicalizing and splitting..."):
                    X_train, X_test, y_train, y_test = (
                        chemicalize_and_prep_dataset(
                            st.session_state["chembl_data"],
                            test_size=test_size,
                            random_state=split_random_state,
                            radius=radius,
                            fpSize=fpSize,
                        )
)

            st.session_state["X_train"] = X_train
            st.session_state["X_test"] = X_test
            st.session_state["y_train"] = y_train
            st.session_state["y_test"] = y_test

            chemicalize_status.success(
                f"Train: {len(X_train)} | Test: {len(X_test)}"
            )


    if train_button:
        if "X_train" not in st.session_state:
            train_status.warning("First chemicalize dataset")
        else:
            with train_status:
                with st.spinner(
                    "Training AutoML model..."):
                    automl, model_score, results_path = auto_ml(
                        X_train=st.session_state["X_train"],
                        y_train=st.session_state["y_train"],
                        X_test=st.session_state["X_test"],
                        y_test=st.session_state["y_test"],
                        chembl_id=chembl_id,
                        model_time_limit=model_time_limit,
                        results_path=results_path,
                        algorithms=algorithms,
                        train_ensemble=train_ensemble,
                        stack_models=stack_models,
                        golden_features=golden_features,
                        features_selection=features_selection,
                        random_state=automl_random_state,
                        explain_level=explain_level,
                        mode=mode,
                        eval_metric=eval_metric,
                        random_seed=random_seed,
                        fpSize=fpSize,
                        radius=radius,
                        folds=folds,
                        n_jobs=n_jobs
                    )

                    st.write(f"Test score: {model_score:.4f}")
                    st.session_state["automl_model"] = automl


            train_status.success(f"""AutoML training completed successfully ✅. 
                                     \nTest score: {model_score:.4f}.
                                     \nFor evaluation of model's performance display  **'README.md'** file in {results_path}""")


elif sbar == "Data Uploading":
    fpSize = st.selectbox("Specify number of bits", options=[pow(2, i) for i in range(10, 14)])
    radius = st.number_input("Choose radius", min_value=1, max_value=4, value=3)

    cpds = st.radio("Choose Data:", ["CSV file", "SMILES string", "De novo generation"])

    if cpds == "CSV file":
        uploaded_file = st.file_uploader("Upload CSV", type="csv")

        if uploaded_file:
            df, X = load_data(uploaded_file, radius=radius, fpSize=fpSize)
            st.session_state["X"] = X
            st.session_state["df"] = df
            st.success("CSV uploaded")
            st.write(df)

    elif cpds == "SMILES string":
        cpd = st.text_input("Paste SMILES string")

        if cpd:
            mol = Chem.MolFromSmiles(cpd)

            if mol:
                morgan_generator = AllChem.GetMorganGenerator(radius=radius, fpSize=fpSize)
                fp = morgan_generator.GetFingerprintAsNumPy(mol)
                fp = fp.reshape(1, -1)
                st.session_state["X"] = fp
                df = pd.DataFrame({"id": ["compound_1"], "smiles": [cpd], "mol": [mol]})
                st.session_state["df"] = df
                st.success("Fingerprint generated")

            else:
                st.error("Invalid SMILES")

    else:
        st.write("Specify generation settings:")
        input_structure = st.text_input("Choose structure, e.g. it can be simple C atom or more complex structure like C1=CC=C2C(=C1)C=CN2", value='C')
        iterations = st.number_input("Number of iterations", min_value=1, value=1000)
        temperature = st.number_input("Temperature", min_value=0.1, max_value=1.0, value=0.9)
        max_new_tokens = st.number_input("Max new tokens", min_value=1, value=50)
        do_sample = st.checkbox("Do sample", value=True)
        repetition_penalty = st.number_input("Number of repetition penalty", min_value=1.0, value=1.1)
        num_beams = st.number_input("Number of beams", min_value=1, value=1)
        top_k = st.number_input("Top k", min_value=1, value=50)
        top_p = st.number_input("Top p", min_value=0.0, max_value=1.0, value=0.9)
        num_return_sequences = st.number_input("Number of return sequences", min_value=1, value=10)

        button= st.button('Run generation')
        if button:
            with st.spinner('Generating molecules...'):
                df = run_lm(smiles=input_structure, iterations=iterations, temperature=temperature, max_new_tokens=max_new_tokens,
                            do_sample=do_sample, repetition_penalty=repetition_penalty, num_beams=num_beams, top_k=top_k, top_p=top_p, num_return_sequences=num_return_sequences,)
                df = df.rename(columns={"mols": "mol"})
                morgan_generator = AllChem.GetMorganGenerator(radius=radius, fpSize=fpSize)
                fps = [morgan_generator.GetFingerprintAsNumPy(mol) for mol in df["mol"]]
                X = np.stack(fps)
                st.session_state["df"] = df
                st.session_state["X"] = X
                st.dataframe(df.drop(columns=["mol"]))



elif sbar == "QSAR prediction":
    models = [dir for dir in os.listdir(os.getcwd()) if dir.endswith('ml_model')]
    choose_model = st.radio("Choose model:", models, index=None)

    if choose_model:
        model_dir = os.path.join(os.getcwd(), choose_model)
        automl = AutoML(results_path=model_dir)

        prediction_button = st.button("Predict")
        if prediction_button:
            if 'X' not in st.session_state:
                st.warning('Upload molecules first')

            else:
                prediction = automl.predict(st.session_state["X"])

                df = st.session_state["df"].copy()
                df["Predicted Label"] = prediction
                st.session_state["df"] = df

                if len(prediction) == 1:
                    st.markdown(f"Predicted activity label: `{prediction[0]}`")
                else:
                    st.dataframe(
                        df[["id", "smiles", "Predicted Label"]].sort_values(
                            by="Predicted Label", ascending=False
                        )
                        )
            active_mols_no = df[df['Predicted Label'] == 1].shape[0]
            st.success(f"{active_mols_no} molecules predicted as biologically active! ({active_mols_no/df.shape[0]:.2f}%)", icon="✅")


elif sbar == 'Molecular Descriptors':
    if "df" not in st.session_state:
        st.warning("Upload compounds first")
        st.stop()
    bioactive_ligands_button = st.checkbox("Calculate descriptors only for active ligands")
    calculate_button = st.button("Calculate descriptors")
    df = st.session_state["df"].copy()

    if bioactive_ligands_button:
        df = df[df['Predicted Label'] == 1]
        if calculate_button:
            with st.spinner("Calculating descriptors..."):
                df = calculate_descriptors(df)
                st.dataframe(df)
    else:
        if calculate_button:
            with st.spinner("Calculating descriptors..."):
                df = calculate_descriptors(df)
                st.dataframe(df)

elif sbar == 'Docking':
    target = st.text_input('Paste path receptor file (.pdbqt)')
    select_active_mols = st.radio('Select scope of molecules for docking', ['Only predicted as active ligands', 'All'])
    if 'df' not in st.session_state:
        st.warning("Upload compounds first")
        st.stop()
    else:
        df = st.session_state["df"].copy()

    if select_active_mols == 'Only predicted as active ligands':
        df = df[df['Predicted Label']==1]
    st.dataframe(df)

    col9, col10, col11 = st.columns(3)
    with col9:
        format_converter_button = st.button('Convert ligands from smiles to .pdbqt')
        if format_converter_button:
            temp_dir_path = os.path.join(os.getcwd(), "temp")
            rmtree(temp_dir_path, ignore_errors=True)
            smiles2pdbqt(df)
            st.success('Molecules converted!')

    with col10:
        grid_center_x = st.number_input('Specify grid center x coordinate', value=0.00)
        grid_center_y = st.number_input('Specify grid center y coordinate', value=0.00)
        grid_center_z = st.number_input('Specify grid center z coordinate', value=0.00)
        grid_size_x = st.number_input('Specify grid size x size', value=20)
        grid_size_y = st.number_input('Specify grid size y size', value=20)
        grid_size_z = st.number_input('Specify grid size z size', value=20)

    with col11:
        exhaustivness = st.number_input('Exhaustiveness', value=8)
        n_poses = st.number_input('Number of poses', value=10)

    docking_button = st.button('Run docking')
    if docking_button:
        perform_docking(target,
                        [grid_center_x, grid_center_y, grid_center_z, grid_size_x, grid_size_y, grid_size_z],
                        exhaustivness,
                        n_poses)
        st.success('Docking completed!')

else:

    st.subheader("Visual inspection")

    uploaded_file_receptor = st.file_uploader("Choose receptor (.pdbqt)",type=["pdbqt"])
    uploaded_file_ligand = st.file_uploader("Choose docking result ligand 1 (.pdbqt)", type=["pdbqt"])
    uploaded_file_ligand2 = st.file_uploader("Choose docking result ligand 2 (.pdbqt) - optional", type=["pdbqt"])

    if uploaded_file_receptor and uploaded_file_ligand:
        receptor = (uploaded_file_receptor.getvalue().decode("utf-8"))
        ligand_pdbqt = (uploaded_file_ligand.getvalue().decode("utf-8"))
        poses, energies = parse_pdbqt_poses(ligand_pdbqt)

        ligand2_pdbqt = None
        poses2 = None
        energies2 = None

        if uploaded_file_ligand2:
            ligand2_pdbqt = (uploaded_file_ligand2.getvalue().decode("utf-8"))
            poses2, energies2 = parse_pdbqt_poses(ligand2_pdbqt)

        st.divider()
        col1, col2 = st.columns([1,3])

        with col1:
            st.subheader("Visualization")
            protein_style = st.selectbox("Protein style",["cartoon", "stick", "line", "sphere", "disable"])
            protein_color = st.selectbox("Protein color",["lightgray", "white", "gray", "blue", "green", "cyan", "yellow", "orange", "red", "purple"])
            protein_opacity = st.slider("Protein opacity", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
            ligand_style = st.selectbox("Ligand style",["stick", "sphere", "line"])
            ligand_colorscheme = st.selectbox("Ligand 1 coloring",["Jmol", "greenCarbon", "cyanCarbon", "magentaCarbon", "yellowCarbon", "purpleCarbon",
                                                                   "orangeCarbon", "whiteCarbon"])

            st.divider()

            pose = st.slider("Ligand 1 pose", min_value=1, max_value=len(poses), value=1)
            st.metric("Ligand 1 affinity", f"{energies[pose-1]:.2f} kcal/mol")


            pose2 = None
            if poses2:
                pose2 = st.slider("Ligand 2 pose", min_value=1, max_value=len(poses2), value=1)
                st.metric("Ligand 2 affinity", f"{energies2[pose2-1]:.2f} kcal/mol")

            st.divider()

            center_on_ligand = st.checkbox("Center camera on ligand", value=True)
            spin = st.checkbox("Rotate structure", value=False)
            show_labels = st.checkbox("Show residue labels", value=True)
            distance_cutoff = st.slider("Contact distance (Å)", min_value=2.0, max_value=8.0, value=5.0, step=0.5)

            st.divider()

            affinity_table = pd.DataFrame({"Ligand 1 Pose": np.arange(1,len(poses)+1), "Affinity (kcal/mol)": energies})
            st.dataframe(affinity_table, use_container_width=True, hide_index=True)


            if poses2:
                affinity_table2 = pd.DataFrame({"Ligand 2 Pose": np.arange(1,len(poses2)+1), "Affinity (kcal/mol)": energies2})
                st.dataframe(affinity_table2, use_container_width=True, hide_index=True)



        with col2:
            contacts = visual_inspection(
                receptor_pdb=receptor,
                ligand_pdb=poses[pose-1],
                ligand2_pdb=(poses2[pose2-1] if poses2 else None),
                distance_cutoff=distance_cutoff,
                protein_style=protein_style,
                ligand_style=ligand_style,
                protein_opacity=protein_opacity,
                protein_color=protein_color,
                ligand_colorscheme=ligand_colorscheme,
                center_on_ligand=center_on_ligand,
                spin=spin,
                show_labels=show_labels
            )

        st.divider()

        st.subheader(f"Residues within {distance_cutoff:.1f} Å")
        if contacts.empty:
            st.info("No contacting residues found.")

        else:
            st.dataframe(contacts, use_container_width=True, hide_index=True)





