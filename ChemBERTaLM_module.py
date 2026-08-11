import streamlit as st
import torch
from transformers import RobertaForCausalLM, RobertaTokenizer, pipeline
from rdkit import Chem
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")


@st.cache_resource
def load_model():
    tokenizer = RobertaTokenizer.from_pretrained("gokceuludogan/ChemBERTaLM")
    model = RobertaForCausalLM.from_pretrained("gokceuludogan/ChemBERTaLM", torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
    device = 0 if torch.cuda.is_available() else -1

    if device == 0:
        model = model.to("cuda")

    generator = pipeline(
        "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=device)

    return generator


class ChemBERT:
    def __init__(
        self,
        smiles: str,
        iterations: int,
        max_new_tokens: int,
        do_sample: bool,
        num_beams: int,
        temperature: float,
        top_k: int,
        top_p: float,
        num_return_sequences: int,
        repetition_penalty: float,
    ):
        self.smiles = smiles
        self.iterations = iterations
        self.max_new_tokens = max_new_tokens
        self.do_sample = do_sample
        self.num_beams = num_beams
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
        self.num_return_sequences = num_return_sequences
        self.repetition_penalty = repetition_penalty

        self.generator = load_model()

    def generate(self, batch_size: int = 32):
        prompts = [self.smiles] * self.iterations
        outputs = self.generator(
            [self.smiles],
            max_new_tokens=self.max_new_tokens,
            do_sample=self.do_sample,
            num_beams=self.num_beams,
            num_return_sequences=self.iterations,
            temperature=self.temperature,
            top_k=self.top_k,
            top_p=self.top_p,
            repetition_penalty=self.repetition_penalty,
        )

        self.l = [seq["generated_text"] for group in outputs for seq in group]

    def sanitize(self):
        mols = []
        smiles_list = []

        for s in self.l:
            mol = Chem.MolFromSmiles(s)
            if mol is not None:
                mols.append(mol)
                smiles_list.append(Chem.MolToSmiles(mol))

        return mols, smiles_list


def combinatorial_synthesis(
    smiles: str,
    iterations: int,
    max_new_tokens: int,
    do_sample: bool,
    num_beams: int,
    temperature: float,
    top_k: int,
    top_p: float,
    num_return_sequences: int,
    repetition_penalty: float,
):

    model = ChemBERT(
        smiles=smiles,
        iterations=iterations,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        num_beams=num_beams,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        num_return_sequences=num_return_sequences,
        repetition_penalty=repetition_penalty,
    )

    model.generate()
    return model.sanitize()

