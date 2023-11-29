import json
from gpa import extract_text_pdf
from gpa import extract_gpa
from edu import extract_education


def details_from_resume(file_path):
    text = extract_text_pdf(file_path)
    gpa = extract_gpa(text)
    # education - need to check the type of output
    education = extract_education(text)

    # work_ex = work_ex.extract_work_ex(text)

    data = {
        "GPA": gpa,
        "Education": education
        # 'Work Experience':work_ex
    }

    with open("ResumeData.json", "w") as f:
        json.dump(data, f, indent=2)


details_from_resume("./resume/resume/Professional CV Resume.pdf")

# gpa out of 4 or 10, and then classify based on high/low
