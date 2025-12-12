import torch
from typing import Optional
from llm.model import load_llm_model

MAX_INPUT_TOKENS = 4096

def build_llm_prompt(text: str) ->str:
    prompt_template = (
        "<bos><start_of_turn>\n"
        "Voce é um especialista na análise de documentos"
        "Gere um resumo conciso, profissional e completo do texto a seguir, em português-BR"
        "O resumo deve ter no máximo 200 palavras.\n\n"
        "---TEXTO A RESUMIR---\n"
        f"{text}" 
        "\n---FIM DO TEXTO---\n"
        "<end_of_turn>\n<start_of_turn>model\n"
    )
    return prompt_template

def generate_summary(full_text: str) -> Optional[str]:

    if not full_text:
        return "Nenhum texto para resumir"
    
    try:
        model, tokenizer = load_llm_model()

        #Chunking para suportar tamanhos de PDF maiores
        input_tokens = tokenizer(full_text, return_tensors="pt", truncation=False, padding=False)
    
        if input_tokens['input_ids'].shape[1] > MAX_INPUT_TOKENS:
            truncated_input_ids = input_tokens['input_ids'][:, :MAX_INPUT_TOKENS]
        
            text_chunk = tokenizer.decode(truncated_input_ids[0], skip_special_tokens=True)
        else:
            text_chunk = full_text

        prompt = build_llm_prompt(text_chunk)
        imput_ids = tokenizer(prompt, return_tensors='pt').to(model.device)

        output_tokens = model.generate(
            **imput_ids,
            max_new_tokens = 256,
            do_sample = True,
            temperature = 0.7,
            pad_token_id = tokenizer.eos_token_id
        ) 

        generated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=False)

        separator = '<start_of_turn>model\n' 
        
        if separator in generated_text:
            
            summary = generated_text.split(separator)[1].strip()
        else:
            prompt_end = prompt.strip() 
            if generated_text.startswith(prompt_end):
                 
                 summary = generated_text[len(prompt_end):].strip()
            else:
                 
                 summary = generated_text.strip()
                 print("Aviso: Separador não encontrado. Retornando texto gerado completo.")

        return summary
    
    except Exception as e:
        print(f"Erro...{e}")
        return None

