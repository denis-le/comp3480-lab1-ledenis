from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Lab 1!"}

@app.get("/about")
async def about():
    return {"message": "This is my FastAPI service!"}

@app.get("/age")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

@app.get("/age/{birth_year}/{current_year}")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

