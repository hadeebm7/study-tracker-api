from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Study Tracker API is running"}
