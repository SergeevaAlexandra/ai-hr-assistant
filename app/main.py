from core.parser import extract_personal_info

if __name__ == "__main__":
    sample_text = """
    Иван Петров
    +7 (999) 123-45-67
    python-разработчик
    """
    result = extract_personal_info(sample_text)
    print(result)