from cli.arguments import arguments, CLIArgs
from pdf.extractor import extract_content, extract_num_pages
from pdf.images import extract_images
from utils.files import get_file_size, save_resumo_file, get_summary_filepath
from utils.text import clean_text, filter_stopwords, get_num_words, get_vocabulary_stats
from llm.summarize import generate_summary

def pdf_analysis(args: CLIArgs):
    
    # Parte para a Extração do pdf e imagens, e análise das informações
    pdf_path = args.pdf_path
    print(f"----- PROCESSANDO PDF: {pdf_path} -----")
    print()

    # Realização da funcionalidades

    num_pages = extract_num_pages(pdf_path)
    file_size = get_file_size(pdf_path)

    full_text = extract_content(pdf_path)
    if not full_text:
        print("Não foi possível extrair o texto do PDF")
        return
    
    words = clean_text(full_text)
    total_words = get_num_words(words)
    no_stopwords_text = filter_stopwords(words)

    vocabulary_size, top_10_words = get_vocabulary_stats(words, no_stopwords_text)

    # Exibição dos resultados

    print("------- RESULTADOS DA ANALISE DO PDF -------")
    print(f"1. Numero total de paginas: {num_pages}")
    print(f"2. Numero total de palavras: {total_words}")
    print(f"3. Tamanho em bytes do arquivo PDF: {file_size}")
    print(f"4. Tamaho do vocabulário: {vocabulary_size}")
    print("\n5.Lista das 10 palavras mais comuns: ")
    for word, count in top_10_words:
        print(f" - {word}: {count}")
    print("--------------------------------------------")

    # Extração e Salvamento de imagens

    print("Extraindo imagens...")

    extract_images(pdf_path)

    # Geração do resumo LLM
    summary = generate_summary(full_text)
    
    if summary:
        print("\n------------- RESUMO GERADO -------------")
        print(summary)
        print("-----------------------------------------\n")

        # Para salvar o resumo em .md
        summary_path = get_summary_filepath(pdf_path=args.pdf_path, output_dir=args.output_dir)
        saved_resumo = save_resumo_file(content=summary, full_path=summary_path)

        if saved_resumo:
            print(f"Resumo salvo em: {saved_resumo}")
        else:
            print("Falha ao salvar resumo")
        

def main():
  
    try:
        args = arguments()
        pdf_analysis(args)

    except Exception as e:
        print(f"\nErro...{e}")

if __name__ == "__main__":
    main()