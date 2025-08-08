from pydantic import BaseModel, Field
from typing import List, Optional

class WorkExperience(BaseModel):
    organization: str = Field(description="Name of the company")
    position: str = Field(description="Position held, e.g., Senior Frontend Developer")
    period: str = Field(description="Work period, e.g., 'Jan 2020 - Present'")
    description: Optional[str] = Field(description="Key responsibilities and achievements")

class Education(BaseModel):
    year : int = Field(description="Graduation year")
    educational_institution: str = Field(description="Example: Oxford university")
    specialty: str = Field(description="Example: Computer Science")

class PersonalInfo(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    place: str = Field(description="Place of residence")
    position: str = Field(description="Current position, e.g., Frontend Developer")
    skills: str = Field(description="Comma-separated skills, e.g., Git")
    work_experience_time: str = Field(description="Example: 5 years")
    work_experiences_description: List[WorkExperience] = Field(
        default_factory=list,
        description="List of work experiences in different organizations"
    )
    education: List[Education] = Field(
        default_factory=list,
        description="List of education"
    )

