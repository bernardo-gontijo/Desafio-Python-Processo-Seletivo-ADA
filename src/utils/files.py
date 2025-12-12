import os
from typing import Union

# Função para conseguir o tamanho em bytes do arquivo

def get_file_size(pdf_path: str) -> Union[int, None]:
    try:
        return os.path.getsize(pdf_path)
    
    except Exception as e:
        print(f"Erro...{e}")
        return None
    
#Função para adicionar o resumo a um arquivo .md 
def save_resumo_file(content: str, full_path: str) -> Union[str, None]:

    try:
        directory = os.path.dirname(full_path) 
        
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return full_path
        
    except Exception as e:
        filename = os.path.basename(full_path)
        print(f"ERRO ao salvar o arquivo '{filename}': {e}")
        return None
    
def get_summary_filepath(pdf_path: str, output_dir: str, extension: str = ".md") -> str:

    pdf_filename = os.path.basename(pdf_path)
    pdf_name_only = os.path.splitext(pdf_filename)[0]
    
    summary_filename = f"{pdf_name_only}_resumo{extension}"
    
    file_path = os.path.join(output_dir, summary_filename)
    
    return file_path

            
    