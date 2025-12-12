import os
import fitz as PyMuPDF
from typing import List

def extract_images(pdf_path: str, output_dir_base: str = "images") -> List[str]:

    # Adquirir os caminhos do arquivo
    pdf_filename = os.path.basename(pdf_path)
    pdf_name_only = os.path.splitext(pdf_filename)[0]
    output_path = os.path.join(output_dir_base, pdf_name_only)

    # Criar o diretório, checagem caso ja exista
    os.makedirs(output_path, exist_ok=True)  

    saved_images_paths = []
    document = None
    
    try:
        document = PyMuPDF.open(pdf_path)

        for page in document:

            # Referencias das imagens
            images = page.get_images()

            for img_idx, image in enumerate(images):
                xref = image[0]

                # Obtenção dos dados binários da imagem
                imgData = document.extract_image(xref)
                imgBytes = imgData['image']
                imgExt = imgData['ext']

                imgFilename = f"{pdf_name_only}_p{page.number + 1}_img{img_idx}.{imgExt}"
                imgPath = os.path.join(output_path, imgFilename)

                with open(imgPath, "wb") as img_file:
                    img_file.write(imgBytes)
                    
                saved_images_paths.append(imgPath)

        print("Imagens extraidas com sucesso!")

    except Exception as e:
        print(f"Erro...{e}")

    finally:
        if document:
            document.close()

    return saved_images_paths
