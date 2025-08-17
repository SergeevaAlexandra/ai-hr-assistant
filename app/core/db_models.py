from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    place = Column(String)
    position = Column(String)
    skills = Column(Text)
    work_experience_time = Column(String)

    work_experiences = relationship("WorkExperience", back_populates="candidate", cascade="all, delete")
    educations = relationship("Education", back_populates="candidate", cascade="all, delete")

class WorkExperience(Base):
    __tablename__ = "work_experiences"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(String, nullable=False)
    position = Column(String, nullable=False)
    period = Column(String)
    description = Column(Text)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    candidate = relationship("Candidate", back_populates="work_experiences")

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    educational_institution = Column(String, nullable=False)
    specialty = Column(String)
    year = Column(String)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    candidate = relationship("Candidate", back_populates="educations")
