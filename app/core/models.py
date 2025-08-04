from pydantic import BaseModel

class PersonalInfo(BaseModel):
    first_name: str
    last_name: str
    phone: str