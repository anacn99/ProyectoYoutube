# archivo main.py
from fastapi import FastAPIapp = FastAPI()@app.get("/")
def read_root():
    return {"Hello": "World"}
