from openbabel import pybel
import os

def smiles2pdbqt(dataframe):
  for sm, idx in zip(dataframe['smiles'], dataframe['id']):
    mol = pybel.readstring("smi", sm)
    mol.addh()
    mol.make3D()
    os.makedirs('converted_ligands', exist_ok=True)
    mol.write("pdbqt", os.path.join(os.getcwd(), f'converted_ligands/{idx}.pdbqt'), overwrite=True)


