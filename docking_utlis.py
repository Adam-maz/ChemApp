from vina import  Vina
import os
import py3Dmol
import io
import streamlit.components.v1 as components
from Bio.PDB import PDBParser, NeighborSearch
import numpy as np
import pandas as pd
import tempfile


def perform_docking(receptor_file, list_of_grid_params, exhaustiveness, n_poses):
    v = Vina(verbosity=0)

    with tempfile.NamedTemporaryFile(suffix=".pdbqt", delete=False) as tmp:
        tmp.write(receptor_file.getbuffer())
        receptor_path = tmp.name

    try:
        v.set_receptor(receptor_path)
        v.compute_vina_maps(center=list_of_grid_params[:3], box_size=list_of_grid_params[3:6])
        path_to_ligands = os.path.join(os.getcwd(), "temp")
        os.makedirs("docking_results", exist_ok=True)

        for lig in os.listdir(path_to_ligands):
            ligand_path = os.path.join(path_to_ligands, lig)
            v.set_ligand_from_file(ligand_path)
            v.dock(exhaustiveness=exhaustiveness, n_poses=n_poses)
            output_path = os.path.join(os.getcwd(), "docking_results", lig.split(".")[0])
            v.write_poses(f"{output_path}_vina_out.pdbqt", n_poses=n_poses, overwrite=True)

    finally:
        os.unlink(receptor_path)


def parse_pdbqt_poses(pdbqt_text):
    poses = []
    energies = []
    current_pose = []
    recording = False

    for line in pdbqt_text.splitlines():
        if line.startswith("MODEL"):
            recording = True
            current_pose = []

        elif line.startswith("ENDMDL"):
            recording = False
            poses.append("\n".join(current_pose))

        elif recording:
            if line.startswith("REMARK VINA RESULT:"):
                energy = float(line.split()[3])
                energies.append(energy)

            elif line.startswith(("ATOM","HETATM")):
                current_pose.append(line)

    return poses, energies



def visual_inspection(
        receptor_pdb,
        ligand_pdb,
        ligand2_pdb=None,
        distance_cutoff=5.0,
        protein_style="cartoon",
        ligand_style="stick",
        protein_opacity=0.5,
        protein_color="lightgray",
        ligand_colorscheme="Jmol",
        center_on_ligand=True,
        spin=False,
        show_labels=True
        ):

    parser = PDBParser(QUIET=True)
    receptor = parser.get_structure("rec", io.StringIO(receptor_pdb))
    ligand = parser.get_structure("lig1", io.StringIO(ligand_pdb))
    ligand2 = None

    if ligand2_pdb:
        ligand2 = parser.get_structure("lig2", io.StringIO(ligand2_pdb))



    ns = NeighborSearch(list(receptor.get_atoms()))
    residues = {}


    def calculate_contacts(lig_structure, ligand_name):
        for lig_atom in lig_structure.get_atoms():
            nearby = ns.search(lig_atom.coord, distance_cutoff, level="R")
            for res in nearby:
                key = (res.get_parent().id, res.id[1])
                min_dist = np.inf

                for atom in res.get_atoms():
                    d = np.linalg.norm(lig_atom.coord - atom.coord)

                    if d < min_dist:
                        min_dist = d

                if key not in residues:
                    residues[key] = {
                        "Ligand": ligand_name,
                        "chain": res.get_parent().id,
                        "resi": res.id[1],
                        "resname": res.resname,
                        "distance": min_dist
                    }

                else:
                    if min_dist < residues[key]["distance"]:
                        residues[key]["distance"] = min_dist


    calculate_contacts(ligand,"Ligand 1")

    if ligand2:
        calculate_contacts(ligand2, "Ligand 2")



    view = py3Dmol.view(width="100%", height=800)
    view.setBackgroundColor("white")



    view.addModel(receptor_pdb, "pdb")
    if protein_style != "disable":
        view.setStyle(
            {"model":0},
            {
                protein_style:{
                    "color":protein_color,
                    "opacity":protein_opacity
                }
            }
        )


    view.addModel(ligand_pdb, "pdb")
    view.setStyle(
        {"model":1},
        {
            ligand_style:{
                "radius":0.22,
                "colorscheme":ligand_colorscheme
            }
        }
    )



    if ligand2_pdb:
        view.addModel(ligand2_pdb, "pdb")
        view.setStyle(
            {"model":2},
            {
                ligand_style:{
                    "radius":0.22,
                    "colorscheme":"greenCarbon"
                }
            }
        )


    for r in residues.values():
        selection = {
            "model":0,
            "chain":r["chain"],
            "resi":r["resi"]}

        view.addStyle(
            selection,
            {
                "stick": {
                    "radius": 0.08,
                    "colorscheme": "default"
                }
            }
        )


        view.addStyle(
            {
                **selection,
                "elem": "C"
            },
            {
                "stick": {
                    "radius": 0.08,
                    "color": "cornflowerblue"
                }
            }
        )


        if show_labels:
            view.addResLabels(
                selection,
                {
                    "fontSize":12,
                    "fontColor":"black",
                    "backgroundColor":"white",
                    "backgroundOpacity":0.8
                }
            )


    if center_on_ligand:
        if ligand2_pdb:
            view.zoomTo({"model":1})
            view.zoom(0.8)

        else:
            view.zoomTo({"model":1})

    else:
        view.zoomTo()


    view.zoom(1.2)


    if spin:
        view.spin(True)

    else:
        view.spin(False)


    components.html(view._make_html(), height=800, scrolling=False)



    df = pd.DataFrame(list(residues.values()))
    if not df.empty:
        df = df.sort_values("distance")
        df.rename(
            columns={
                "chain":"Chain",
                "resi":"Residue ID",
                "resname":"Residue",
                "distance":"Distance (Å)"},
            inplace=True)

        df["Distance (Å)"] = (df["Distance (Å)"].round(2))

    return df