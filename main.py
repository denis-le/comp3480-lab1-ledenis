from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# Simple Route
@app.get("/")
async def root():
    return {"message": "Hello Lab 1!"}

# Simple Route
@app.get("/about")
async def about():
    return {"message": "This is my FastAPI service!"}

# Query String Route
@app.get("/age")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

# Path Route
@app.get("/age/{birth_year}/{current_year}")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

class PersonInput(BaseModel):
    name: str
    birth_year: int
    current_year: int

# Post Route with Pydantic
@app.post("/person")
async def person_age(person: PersonInput):
    return {"message": f"{person.name}, You are {person.current_year - person.birth_year} years old!"}


