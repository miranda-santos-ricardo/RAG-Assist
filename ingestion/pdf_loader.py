import PyPDF2

def load_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text_chunks = ""
    for page in pdf_reader.pages:
        text_chunks += page.extract_text() +"\n"
    return text_chunks

