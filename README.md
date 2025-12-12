# Desafio-Python-Processo-Seletivo-ADA
Este desafio faz parte do processo seletivo para a bolsa Trainee LLM do Projeto ADA – Assembly Digital Assistant, cujo foco é avaliar sua capacidade de organizar um projeto em Python, manipular arquivos, extrair informações estruturais de um PDF e integrar uma LLM local usando Hugging Face.

**INFORMAÇÕES NECESSÁRIAS**

Para ativação do ambiente virtual: .venv\Scripts\activate

Para instalar as bibliotecas necessárias: pip install -r requirements.txt

**ENTRADA:**

Para iniciar o programa digite o seguinte comando no bash: python src/main.py --pdf nome-do-pdf.pdf

**Explicações**

*Ao iniciar o algoritmo com a entrada correta serão exibidos:*
    1. Número total de páginas
    2. Número total de palavras
    3. Tamanho em bytes do arquivo PDF
    4. Tamanho do vocabulário 
    5. Lista das 10 palavras mais comuns 

*Além disso:*
    Serão criadas as pastas/arquivos:
        images: Com as imagens do pdf identificadas
        nome-do-pdf.md: Com o resumo gerado por LLM (Gerados pelo modelo local do Hugging Face, mais especificamente Gemma-2B-IT)
