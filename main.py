from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

subjects = []


class Subject(BaseModel):
    name: str


@app.get("/")
def root():
    return {"message": "Hello from my first API"}


@app.post("/subjects")
def add_subject(subject: Subject):
    subjects.append(subject.name)
    return {"message": "Subject added", "subjects": subjects}


@app.get("/subjects")
def list_subjects():
    return {"subjects": subjects}


@app.get("/subjects/count")
def count_subjects():
    return {"count": len(subjects)}

@app.delete("/subjects/{name}")
def delete_subject(name: str):
    if name not in subjects:
        raise HTTPException(status_code=404, detail="Subject not found")
    subjects.remove(name)
    return {"message": "Subject deleted", "subjects": subjects}