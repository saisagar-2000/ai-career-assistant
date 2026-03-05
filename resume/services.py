import pdfplumber


import pdfplumber
from ai_engine.resume_analyzer import analyze_resume


def extract_resume_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def process_resume(resume):

    text = extract_resume_text(resume.file.path)

    ai_feedback = analyze_resume(text)

    return {
        "resume_id": resume.id,
        "analysis": ai_feedback
    }