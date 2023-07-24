from extract_text import extract_res
from extract_info import resume_extract
from generate_json import generate_json




resume_path = 'Sanjaya_Maharana_3.5_yoe.pdf'
extracted_text = extract_res(resume_path)
extracted_info = resume_extract(extracted_text)
json_data = generate_json(extracted_info)
