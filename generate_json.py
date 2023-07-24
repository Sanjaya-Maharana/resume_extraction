import json
def formatted_json(data):
    json_data = {
        "data": {
            "name": {
                "raw": data["Name"]
            },
            "phoneNumbers": [data["Personal Information"]["Phone"]] if data["Personal Information"]["Phone"] else [],
            "websites": [data["Personal Information"]["LinkedIn"], data["Personal Information"]["GitHub"]] if data["Personal Information"]["LinkedIn"] or data["Personal Information"]["GitHub"] else [],
            "emails": [data["Personal Information"]["Email"]] if data["Personal Information"]["Email"] else "",
            "dateOfBirth": "",
            "location": {
                "formatted": ""
            },
            "objective": "",
            "languages": [],
            "totalYearsExperience": "",
            "education": [
                {
                    "id": 0,
                    "organization": "",
                    "accreditation": {
                        "education": "",
                        "educationLevel": ""
                    },
                    "grade": "",
                    "location": {
                        "formatted": ""
                    },
                    "dates": {
                        "completionDate": "",
                        "isCurrent": False,
                        "startDate": ""
                    }
                }
            ],
            "profession": "",
            "linkedin": data["Personal Information"]["LinkedIn"] if data["Personal Information"]["LinkedIn"] else "",
            "workExperience": [
                {
                    "id": 0,
                    "jobTitle": "",
                    "organization": "",
                    "location": "",
                    "dates": {
                        "startDate": "",
                        "endDate": "",
                        "monthsInPosition": 0,
                        "isCurrent": False
                    },
                    "occupation": {
                        "jobTitle": ""
                    }
                }
            ],
            "skills": data["Skills and Technologies"],
            "projects": data["Projects"],
            "certifications": data["Awards"]
        }
    }

    return json_data

def generate_json(data):
    json_data = formatted_json(data)

    with open("output.json", "w") as file:
        json.dump(json_data, file, indent=2)
    return json_data

