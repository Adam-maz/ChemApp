from openbabel import pybel
import os

def smiles2pdbqt(dataframe):
  for sm, idx in zip(dataframe['smiles'], dataframe['id']):
    mol = pybel.readstring("smi", sm)
    mol.addh()
    mol.make3D()
    os.makedirs('temp', exist_ok=True)
    mol.write("pdbqt", os.path.join(os.getcwd(), f'temp/{idx}.pdbqt'), overwrite=True)


