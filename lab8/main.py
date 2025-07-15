from fastapi import FastAPI, Header, Cookie
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
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

# Header Parameters
@app.get("/headers/")
async def read_items(user_email: Optional[str] = Header(None), user_role: Optional[str] = Header(None),
                     device_type: Optional[str] = Header(None)):
    print("Headers received:")
    print(user_email)
    print(user_role)
    print(device_type)
    return {"user-email": user_email, "user-role": user_role, "device-type": device_type}

# Cookie Parameters for light or dark theme
@app.get("/theme")
async def readCookie(theme: Optional[str] = Cookie(None)):
    print("Cookies received:")
    print(theme)
    return {"theme": theme}
