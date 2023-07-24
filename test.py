import json
import re
import PyPDF2
import docx2txt
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            text = ""
            for page_number in range(num_pages):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()
            return text
    except PyPDF2.PdfReadError as e:
        print(f"Error occurred while extracting text from PDF: {e}")
        return None
    except FileNotFoundError as e:
        print(f"PDF file not found: {e}")
        return None



def extract_text_from_word(docx_path):
    try:
        text = docx2txt.process(docx_path)
        return text
    except FileNotFoundError as e:
        print(f"Error occurred while extracting text from Word document: {e}")
        return None


def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except FileNotFoundError as e:
        print(f"Error occurred while extracting text from image: {e}")
        return None


# The remaining code for extracting personal info, education, experience, skills, and projects remains the same.


# Example usage of the modified code
resume_path = r"C:\Users\ACER\PycharmProjects\resume_extraction\resumes\resumes (1).pdf"
resume_text = extract_text_from_pdf(resume_path)
if resume_text:
    # Extract other information from the resume text
    personal_info = extract_personal_info(resume_text)
    education_info = extract_education(resume_text)
    experience = extract_work_experience(resume_text)
    skills = extract_skills(resume_text)
    projects = extract_projects(resume_text)

    # Create a dictionary for the final data
    data = {
        "Name": personal_info["Name"],
        "Personal Information": personal_info,
        "Education": education_info,
        "Work Experience": experience,
        "Skills and Technologies": skills,
        "Projects": projects
    }

    # Convert the data to JSON format
    json_data = json.dumps(data, indent=4)

    # Define the output file path
    output_file = f"{data['Name']}.json"

    # Save the JSON data to the output file
    with open(output_file, "w") as file:
        file.write(json_data)

    # Print a message indicating the successful saving of the JSON data
    print(f"JSON data has been saved to {output_file}.")
