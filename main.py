from extract_text import extract_res
from extract_info import resume_extract
from generate_json import generate_json




resume_path = 'resumessamples/resumes (4).docx'
extracted_text = extract_res(resume_path)
print(extracted_text)
print('*'*150)
print('\n')
extracted_info = resume_extract(extracted_text)
print('\n')
print(extracted_info)
print('*'*150)
print('\n')
json_data = generate_json(extracted_info)
print('\n')
print(json_data)
