from app.core.extractor import extract_personal_info
from app.core.parser import parsing_documents

if __name__ == "__main__":
    file_name = "data/Resume Frontender.docx"
    text_md = parsing_documents(file_name)
    result = extract_personal_info(text_md)
    print(result)