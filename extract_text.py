import PyPDF2
import docx2txt
import pytesseract
import email
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_email(eml_path):
    with open(eml_path, 'r', encoding='utf-8') as file:
        msg = email.message_from_file(file)
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    body += part.get_payload(decode=True).decode(errors='ignore')
        else:
            body = msg.get_payload(decode=True).decode(errors='ignore')
        return body


def extract_text_from_pdf(file_path):
    # Extract text from PDF using PyPDF2 library
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
        return text

def extract_text_from_word(docx_path):
    # Extract text from Word document using docx2txt library
    text = docx2txt.process(docx_path)
    return text

def extract_text_from_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Perform OCR to extract text from the image
    text = pytesseract.image_to_string(image)

    return text


def extract_res(resume_path):
    if resume_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_path.endswith('.docx'):
        resume_text = extract_text_from_word(resume_path)
    elif resume_path.endswith('.eml'):
        resume_text = extract_text_from_email(resume_path)
    else:
        resume_text = extract_text_from_image(resume_path)
    return resume_text

