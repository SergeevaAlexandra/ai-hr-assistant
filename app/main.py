from fastapi import FastAPI, File, UploadFile, Depends, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import tempfile

from sqlalchemy.orm import Session
from app.core.extractor import extract_personal_info
from app.core.parser import parsing_documents
from app.core.database import SessionLocal, engine, Base
from app.core import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === Загрузка и сохранение резюме ===
@app.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text_md = parsing_documents(tmp_path)
    result = extract_personal_info(text_md)

    # сохраняем в БД
    candidate = crud.create_candidate(db, result)

    return JSONResponse(content={"id": candidate.id, "message": "Кандидат сохранён"})


# === Поиск кандидата по имени и фамилии ===
@app.get("/search")
def search_candidate(
    first_name: str = Query(...),
    last_name: str = Query(...),
    db: Session = Depends(get_db)
):
    candidates = crud.get_candidate_by_name(db, first_name, last_name)
    if not candidates:
        return JSONResponse(content={"message": "Кандидат не найден"})
    return candidates


# === Получение кандидата по ID ===
@app.get("/candidates/{candidate_id}")
def read_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = crud.get_candidate_by_id(db, candidate_id)
    if not candidate:
        return JSONResponse(content={"message": "Кандидат не найден"})
    return candidate