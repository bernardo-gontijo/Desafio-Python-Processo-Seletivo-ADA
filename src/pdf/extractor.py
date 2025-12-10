import fitz as PyMuPDF

 # Extrair numero de paginas do .pdf

def extract_num_pages(pdf_path: str):
    document = PyMuPDF.open(pdf_path)
    num_pages = document.page_count
    document.close()

    return num_pages

# Extrair texto do pdf

def extract_content(pdf_path: str):
    fullText = ""
    numPages = 0

    try:
        document = PyMuPDF.open(pdf_path)
        numPages = document.page_count
        
        for page_num in range(numPages): # Para cada pagina 
                page = document.load_page(page_num)
                fullText += page.get_text()

        document.close()

    except Exception as e:
        print(f"ERRO durante a extração do PDF: {e}")
        return ""
    
    return fullText