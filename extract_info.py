
import re
from generate_json import generate_json

def extract_personal_info(text):
    # Regular expression patterns
    name_pattern = r"\b[A-Z][a-zA-Z.'\-\s]+\b" # Matches the name at the beginning of the text
    phone_pattern = r"PHONE:\s*(.*)"
    phone_pattern1 = r"\d{10}"
    phone_pattern2 = r"\+\d{12}"
    phone_pattern3 = r'\+91\s?\d{10}'
    phone_pattern4 = r'\+91-\d{2}-\d{4} \d{4}'
    phone_pattern5 = r"\d{4} \d{7}"
    linkedin_pattern = r"LINKEDIN:\s*(.*)"
    linkedin_pattern1 = r"https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+/?"
    linkedin_pattern2 = r"(?:https?://(?:www\.)?)?linkedin\.com/in/[a-zA-Z0-9_-]+/?"
    github_pattern = r"GITHUB:\s*(.*)"
    github_pattern1 = r"(?:https?://)?github\.com/[a-zA-Z0-9_-]+/?"


    try:
        name_pattern1 = r'''name :"\b[a-zA-Z][a-zA-Z.'\-\s]+\b"'''
        text = text.replace(' "','"')
        print('text',text)
        names = re.findall(name_pattern1, text)
        print(names)
        names[0] = names[0].replace('name :','').replace('"','')
        print(names)
    except:
        names = re.findall(name_pattern, text)
    phone_match = re.search(phone_pattern, text) or re.search(phone_pattern1, text) or re.search(phone_pattern2, text) or \
                  re.search(phone_pattern3, text) or re.search(phone_pattern4, text) or re.search(phone_pattern5, text)
    email_pattern = r"EMAIL:\s*(.*)"
    email_pattern1 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    email_match = re.search(email_pattern, text) or re.search(email_pattern1, text)
    email = email_match.group() if email_match else None
    if email_match== None:
        email_pattern = r"EMAIL:\s*(.*)"
        email_pattern1 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        mail_text = text.replace('\n', '')
        email_match = re.search(email_pattern, mail_text) or re.search(email_pattern1, mail_text)
        email = email_match.group() if email_match else None
        mail_li = email.split('mail')
        mail_li= mail_li[1]+mail_li[2]
        email = mail_li.replace('WWWhttps','')
    email = email.replace('EMAIL:', '').replace('\n', '').replace(' ', '')
    linkedin_match = re.search(linkedin_pattern, text) or re.search(linkedin_pattern1, text) or re.search(linkedin_pattern2, text)
    github_match = re.search(github_pattern, text) or re.search(github_pattern1, text)
    # Get the extracted information
    names = [name.split('\n')[0] for name in names if name != 'Name']
    name = names[0]
    phone = phone_match.group() if phone_match else None
    phone = phone.replace('PHONE:','').replace('\n','').replace(' ','')
    linkedin = linkedin_match.group() if linkedin_match else None
    try:
        linkedin = linkedin.replace('LINKEDIN:', '').replace('\n', '').replace(' ', '')
    except:
        linkedin = linkedin

    github = github_match.group() if github_match else None
    try:
        github = github.replace('GITHUB:', '').replace('\n', '').replace(' ', '')
    except:
        github =github

    # Create a dictionary for personal information
    personal_info = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "LinkedIn": linkedin,
        "GitHub": github
    }

    return personal_info

def extract_education(text):
    # Regular expression pattern to match the education section
    education_pattern = r"EDUCATION:(.*?)(?=(IT SKILLS &TECHNOLOGIES:|WORK EXPERIENCE:|PROJECTS:|$))"
    education_pattern1 = r"(EDUCATION|Education)(.*?)(?=(IT SKILLS &TECHNOLOGIES:|WORK EXPERIENCE:|PROJECTS:|$))"

    # Extract education information
    education_match = re.search(education_pattern, text, re.DOTALL) or re.search(education_pattern1, text, re.DOTALL)

    # Get the extracted education information
    education = education_match.group().strip() if education_match else None
    education = education.replace('EDUCATION:','').replace('Technology','')
    education_cleaned = education.strip()
    education_list = education_cleaned.split('\n \n \n')
    return education_list

def extract_work_experience(text):
    # Regular expression pattern to match the work experience section
    experience_pattern = r"WORK EXPERIENCE:| Experience: |Professional Experience|EXPERIENCE(.*?)(?=(PROJECTS:|Skills|$))"
    experience_pattern1 = r"INTERNSHIP|Work History(.*?)(?=(PROJECTS:|$))"

    # Extract work experience
    experience_match = re.search(experience_pattern, text, re.DOTALL) or re.search(experience_pattern1, text, re.DOTALL)
    experience = experience_match.group().replace("  ",'').strip() if experience_match else None


    return experience

def extract_projects(text):
    # Regular expression pattern to match the projects section
    projects_pattern = r"PROJECTS:(.*?)(?=$)"
    projects_pattern1 = r"(PROJECTS|CERTIFICATION / PROJECT:|Projects :)(.*?)(?=$)"

    # Extract projects
    projects_match = re.search(projects_pattern, text, re.DOTALL) or re.search(projects_pattern1, text, re.DOTALL)
    projects = projects_match.group().replace("  ",'').strip() if projects_match else None

    return projects

def extract_skills(text):
    # Regular expression pattern to match the skills and technologies section
    skills_pattern = r"(IT SKILLS &TECHNOLOGIES:|SKILLS|Front -end Technologies:)(.*?)(?=(WORK EXPERIENCE:|Bachelor of Engineering|INTERNSHIP|INTERN|PROJECTS|ACTIVITIES|PROJECTS:|$))"
    skills_pattern1 = r"(TECHNICAL SKILLS|Skills|Software Skills:)(.*?)(?=(WORK EXPERIENCE:|INTERNSHIP|INTERN|ACTIVITIES|Professional Work Experience:|Language|PROJECTS:|$))"

    # Extract skills and technologies
    skills_match = re.search(skills_pattern, text, re.DOTALL) or re.search(skills_pattern1, text, re.DOTALL)
    skills = skills_match.group().strip() if skills_match else None

    # Remove the \uf0b7 character from the skills
    try:
        skills = re.sub(r"\uf0b7", "", skills)
    except:
        skills = skills
    try:
        skills = skills.replace('IT SKILLS &TECHNOLOGIES:','')
        skills_list = [skill.strip() for skill in skills.split("\n") if skill.strip()]
    except:
        skills_list = None

    return skills_list

def extract_awards(text):
    awards_pattern = r"(AWARDS & HONOURS:|ACHIEVEMENTS)(.*?)(?=$)"
    awards_match = re.search(awards_pattern, text, re.DOTALL)
    awards = awards_match.group().replace("  ", '').strip() if awards_match else None
    return awards



def resume_extract(resume_text):
    # Extract specific sections from the resume text
    personal_info = extract_personal_info(resume_text)
    education_info = extract_education(resume_text)
    experience = extract_work_experience(resume_text)
    skills = extract_skills(resume_text)
    projects = extract_projects(resume_text)
    awards = extract_awards(resume_text)

    # Create a dictionary for the final data
    data = {
        "Name": personal_info["Name"],
        "Personal Information": personal_info,
        "Education": education_info,
        "Work Experience": experience,
        "Skills and Technologies": skills,
        "Projects": projects,
        "Awards": awards
    }
    return data