from .models import PersonalInfo
from ollama import chat
from ollama import ChatResponse
import re
import json

def clean_model_output(text: str) -> str:
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)

def extract_personal_info(text: str) -> PersonalInfo:
    schema_example = PersonalInfo.schema_json(indent=2)

    system_prompt  = f"""
    You're an HR assistant. Extract the necessary information from the text.
    Please respond ONLY in the JSON format strictly conforming to this scheme.

    {schema_example}

    An example of a correct answer:

    {{
      "first_name": "Иван",
      "last_name": "Петров",
      "phone": "+79184761123"
    }}
    """
    try:
        response: ChatResponse = chat(
                model='qwen3:4b',  
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"Резюме:\n{text}"}
                ],
                options={'temperature': 0.1},
                format='json',
                think=False  
            )
        
        raw_response = response['message']['content']
        clean_json = clean_model_output(raw_response)
        data = PersonalInfo.model_validate_json(clean_json)

        return clean_json
    
    except json.JSONDecodeError:
        raise ValueError(f"Невалидный JSON: {clean_json}")
    except Exception as e:
        raise RuntimeError(f"Ошибка: {str(e)}")

