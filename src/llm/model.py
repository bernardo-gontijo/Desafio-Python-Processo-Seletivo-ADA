import torch
from typing import Optional, Tuple
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "google/gemma-2b-it"

model: Optional[AutoModelForCausalLM] = None
tokenizer: Optional[AutoTokenizer] = None

def load_llm_model() -> Tuple[AutoModelForCausalLM, AutoTokenizer]:

    global model, tokenizer

    if model is None or tokenizer is None:
        try:
            tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", dtype=torch.bfloat16)
            print("Modelo LLM carregado com succeso! E esta sendo gerado, isso pode demorar alguns minutos...")

        except Exception as e:
            print(f"Erro...{e}")
            raise

    return model, tokenizer
