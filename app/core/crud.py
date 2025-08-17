from sqlalchemy.orm import Session
from app.core import db_models

def create_candidate(db: Session, candidate_data: dict):
    """Создание кандидата в базе данных"""
    work_experiences = candidate_data.pop("work_experiences", [])
    educations = candidate_data.pop("educations", [])

    db_candidate = db_models.Candidate(**candidate_data)

    for exp in work_experiences:
        db_candidate.work_experiences.append(db_models.WorkExperience(**exp))
    for edu in educations:
        db_candidate.educations.append(db_models.Education(**edu))

    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def get_candidate_by_id(db: Session, candidate_id: int):
    """Получение кандидата по ID"""
    return db.query(db_models.Candidate).filter(db_models.Candidate.id == candidate_id).first()

def get_candidate_by_name(db: Session, first_name: str, last_name: str):
    """Получение кандидата по имени"""
    return db.query(db_models.Candidate).filter(
        db_models.Candidate.first_name == first_name,
        db_models.Candidate.last_name == last_name
    ).all()

def get_all_candidates(db: Session):
    """Получение всех кандидатов"""
    return db.query(db_models.Candidate).all()

def delete_candidate(db: Session, candidate_id: int):
    """Удаление кандидата"""
    candidate = db.query(db_models.Candidate).filter(db_models.Candidate.id == candidate_id).first()
    if candidate:
        db.delete(candidate)
        db.commit()
        return True
    return False

def update_candidate(db: Session, candidate_id: int, update_data: dict):
    """Обновление информации о кандидате"""
    candidate = db.query(db_models.Candidate).filter(db_models.Candidate.id == candidate_id).first()
    if candidate:
        for key, value in update_data.items():
            if hasattr(candidate, key):
                setattr(candidate, key, value)
        db.commit()
        db.refresh(candidate)
        return candidate
    return None