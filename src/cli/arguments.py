import os
import argparse
from typing import NamedTuple, Any

class CLIArgs(NamedTuple):
    pdf_path: str

def create() -> argparse.ArgumentParser:
    
    # Configura os argumento do parser
    parser = argparse.ArgumentParser(description="EXTRAIDOR DE PDF E GERADOR DE RESUMO LLM", formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('--pdf', type = str, required = True, help = "Caminho completo para o arquivo PDF de entrada em português")
    parser.add_argument('--output-dir', type = str, default = '.', help = 'Diretório base onde os Resumos e adicionais serão salvos')

    return parser

def arguments() -> CLIArgs:

    # Analizar os argumentos para o caminho do PDF
    parser = create()
    args = parser.parse_args()

    #Tratamento de exceções 
    if not os.path.exists(args.pdf):
        parser.error(f"Erro...Arquivo não encontrado em: '{args.pdf}'")

    if not args.pdf.lower().endswith('.pdf'):
        parser.error(f"Erro...Arquivo não é um pdf")

    return CLIArgs(pdf_path = args.pdf)