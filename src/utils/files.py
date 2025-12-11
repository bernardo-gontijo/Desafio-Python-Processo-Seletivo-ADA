import os
from typing import Union

# Função para conseguir o tamanho em bytes do arquivo

def get_file_size(pdf_path: str) -> Union[int, None]:
    try:
        return os.path.getsize(pdf_path)
    
    except Exception as e:
        print(f"Erro...{e}")
        return None