from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

# Root
@app.get("/")
async def root():
    return {"message": "Hello Lab 1!"}

# About
@app.get("/about")
async def about():
    return {"message": "This is my FastAPI service!"}

# Year using datetime
@app.get("/year")
async def year():
    return {"message": f"The year is now {datetime.now().year}!"}

# Time using datetime
@app.get("/time")
async def time():
    return {"message": f"The time is now {datetime.now().time()}!"}

# Day of the Week using datetime
@app.get("/day")
async def day():
    return {"message": f"The day is now {datetime.now().strftime('%A')}!"}

# Query String Route for Age
@app.get("/age")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

# Path Route for Age
@app.get("/age/{birth_year}/{current_year}")
async def age(birth_year: int, current_year: int):
    return {"message": f"You are {current_year - birth_year} years old!"}

class PersonInput(BaseModel):
    name: str
    birth_year: int
    current_year: int

# Post Route with Pydantic for Age
@app.post("/person")
async def person_age(person: PersonInput):
    return {"message": f"{person.name}, You are {person.current_year - person.birth_year} years old!"}

# Query String Route for Greeting
@app.get("/name")
async def name(names: str):
    return {"message": f"Hello {names}!"}

# Path String Route for Name
@app.get("/name/{names}")
async def name(names: str):
    return {"message": f"Hello {names}!"}


