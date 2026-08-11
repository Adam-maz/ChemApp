https://github.com/user-attachments/assets/a36df5b8-004d-41d8-adf7-3ed0414c452e

ChemApp
ChemApp is a Streamlit-based application designed to support virtual screening and early-stage drug discovery workflows.
The application integrates machine learning, automated machine learning (AutoML), molecular fingerprinting, de novo molecular generation, drug-likeness assessment, molecular docking, and interactive visualization into a single computational platform.
ChemApp is primarily designed to run in a Linux environment and can also be used under Windows Subsystem for Linux (WSL). For convenience, the application can be launched from Windows using a `.bat` script and a desktop shortcut.
---
🧬 Overview
ChemApp provides an integrated workflow for computational screening and prioritization of potentially bioactive molecules.
The application combines ligand-based machine learning prediction with drug-likeness assessment and structure-based molecular docking.
The main workflow is:
<p align="center"> <img width="550" alt="Chemapp_fig" src="https://github.com/user-attachments/assets/7e862e44-30f9-4187-8669-07e71304b6c9" /> </p>
Importantly, molecular descriptors used for drug-likeness assessment are not used as input features for the machine learning model. The ML model uses molecular fingerprints as its representation.
---
🚀 Features
1. 🧠 Machine Learning Model Development
ChemApp allows users to create a machine learning classification model for molecular bioactivity prediction.
The model development workflow can retrieve experimental bioactivity data directly from ChEMBL using the ChEMBL API.
The user can provide a ChEMBL ID, after which the application retrieves the corresponding dataset and preprocesses it for machine learning.
ChemApp supports datasets based on activity measurements such as:
Ki
IC50
The retrieved data is subsequently processed and converted into molecular representations suitable for machine learning.
ChemApp uses AutoML to automate the process of model development.

---
2. 🧪 Molecular Input
Once a classification model is available, ChemApp provides several ways to obtain molecules for prediction.
Single molecule
A user can enter an individual molecule using its SMILES representation.
Example:
```text
CCO
```
The molecule is then processed and passed to the trained ML model.
Molecular library from CSV
ChemApp can also import a collection of molecules from a `.csv` file.
For example:
```csv
smiles,id
CCO,cpd1
CCN,cpd2
c1ccccc1,cpd3
CC(=O)Oc1ccccc1C(=O)O,cpd4
```
This allows multiple compounds to be screened in a single workflow.
De novo molecular generation
ChemApp can generate new molecular structures using ChemBERTaLM – Hugging Face Model.
The generated molecules can then be passed through the same screening pipeline as externally supplied compounds.

---
3. 🔬 ML Bioactivity Prediction
After molecules have been imported or generated, ChemApp can use the previously trained classification model to predict their bioactivity.
The ML prediction uses molecular fingerprints, consistent with the representation used during model training.
The predicted bioactivity can be used as an initial filtering or prioritization step before further computational analysis.
---
4. 💊 Drug-Likeness Assessment
After bioactivity prediction, ChemApp calculates molecular descriptors used to assess drug-likeness.
These descriptors are not used as features by the ML model. They represent a separate stage of the workflow intended to characterize the physicochemical properties of candidate molecules.
---
5. ⚗️ Molecular Docking
ChemApp integrates molecular docking using AutoDock Vina.
Docking is performed for molecules after the preceding screening steps.
The purpose of this stage is to investigate potential interactions between candidate ligands and a selected protein target.
---
6. 🧊 Docking Visualization
ChemApp provides interactive visualization of docking results using py3Dmol.
---
📦 Installation
1. Clone the repository
```bash
git clone https://github.com/Adam-maz/ChemApp.git
cd ChemApp
```
---
2. Create a virtual environment
Create Conda environment:
```bash
conda env create -f chemapp_environment.yml
```
Activate it:
```bash
conda activate chemapp_env
```
---
▶️ Running the Application
After activating the virtual environment, ChemApp can be started using:
```bash
streamlit run ChemApp.py
```
Streamlit will start a local web server.
The application is typically available at:
```text
http://localhost:8501
```
The exact address and port are displayed by Streamlit when the application starts.
---
🚀 Quick Launch Using a `.bat` Script
For convenience, ChemApp can be launched from Windows using a `.bat` file.
The batch script can start the application inside WSL, making it possible to launch ChemApp using a Windows desktop shortcut.
A simplified example is:
```bat
@echo off

wsl bash -c "cd /path_to_ChemApp && source .run_chemapp.sh"

pause
```
The path should be adjusted to the actual location of the ChemApp project.
The `.bat` file can then be linked to a Windows desktop shortcut.
run_chemapp.sh script and .ico file are also provided
---
📁 Project Structure
A possible project structure is:
```text
ChemApp/
│
├── ChemApp.py
├── .streamlit
├── converted_ligands
├── docking_results
├── chemapp_environment.yml
├── ChemBERTaLM_module.py
├── chembl_auto_ml.py
├── docking_utils.py
├── mol_format_converter.py
├── run_chemapp.sh
├── ml_model_dir
```
The exact structure depends on the current implementation of the project.
---
⚠️ Limitations
ChemApp is intended as a computational research and educational tool for virtual screening and early-stage drug discovery.
The results generated by the application are subject to the limitations of the underlying computational methods.
Potential limitations include:
Dependence on the quality and representativeness of ChEMBL data
Experimental noise in bioactivity measurements
Potential bias in training datasets
Applicability-domain limitations of ML models
Limitations of molecular fingerprints
Uncertainty associated with ML predictions
Simplifications introduced by drug-likeness descriptors
Approximate nature of molecular docking
Limitations of docking scoring functions
Limited representation of protein flexibility
Possible generation of chemically undesirable structures by generative models
Therefore, ChemApp should be considered as a tool for molecular screening, candidate prioritization, and hypothesis generation rather than a replacement for experimental validation.
Experimental studies are required to confirm predicted biological activity and molecular binding.
---
🔬 Intended Use
ChemApp can be used for:
Virtual screening
Early-stage drug discovery
Computational chemistry
Cheminformatics
Bioactivity prediction
Machine learning model development
Automated machine learning
Molecular fingerprint-based classification
De novo molecular generation
Drug-likeness assessment
Molecular docking
Docking pose analysis
Protein–ligand visualization
Computational chemistry education
---
📚 References & Resources
Bioactivity database
ChEMBL
Molecular generation
ChemBERTaLM – Hugging Face
Machine learning
MLJAR Supervised
scikit-learn
PyTorch
Cheminformatics
RDKit
Open Babel
Molecular docking
AutoDock Vina
Visualization & application framework
Streamlit
Plotly
py3Dmol
