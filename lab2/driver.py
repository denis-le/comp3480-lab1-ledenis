import requests
from datetime import datetime

def print_routes():
    print("\nRoutes")
    routes = [
        "0. Exit Driver",
        "1. Root",
        "2. About",
        "3. Year",
        "4. Time",
        "5. Day of the Week",
        "6. Age (query)",
        "7. Age (path)",
        "8. Age (post)",
        "9. Greet (query)",
        "10. Greet (path)",
        "11. Headers",
        "12. Theme (cookies)"
    ]
    for route in routes:
        print(route)

def call_root():
    url = "http://localhost:8080/"
    response = requests.get(url)
    print(response.json())

def call_about():
    url = "http://localhost:8080/about"
    response = requests.get(url)
    print(response.json())

def call_year():
    url = "http://localhost:8080/year"
    response = requests.get(url)
    print(response.json())

def call_time():
    url = "http://localhost:8080/time"
    response = requests.get(url)
    print(response.json())

def call_day():
    url = "http://localhost:8080/day"
    response = requests.get(url)
    print(response.json())

def call_age_query():
    birth_year = input("Enter birth year: ")
    current_year = datetime.today().year
    url = f"http://localhost:8080/age?birth_year={birth_year}&current_year={current_year}"
    response = requests.get(url)
    print(response.json())

def call_age_path():
    birth_year = input("Enter birth year: ")
    current_year = datetime.today().year
    url = f"http://localhost:8080/age/{birth_year}/{current_year}"
    response = requests.get(url)
    print(response.json())

def call_age_post():
    data = {
        "name" : input("Enter name: "),
        "birth_year": input("Enter birth year: "),
        "current_year": datetime.today().year
    }
    url = f"http://localhost:8080/person"
    response = requests.post(url, json=data)
    print(response.json())

def call_name_query():
    name = input("Enter name: ")
    url = f"http://localhost:8080/name?names={name}"
    response = requests.get(url)
    print(response.json())

def call_name_path():
    name = input("Enter name: ")
    url = f"http://localhost:8080/name/{name}"
    response = requests.get(url)
    print(response.json())

def call_headers():
    email = input("Enter email: ")
    role = input("Enter role: ")
    device = input("Enter device type: ")
    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "CustomValue",
        "user-email": email,
        "user-role": role,
        "device-type": device
    }
    url = "http://localhost:8080/headers"
    response = requests.get(url=url, headers=headers)
    print(response.json())

def call_theme():
    theme = input("Enter theme (light or dark): ")
    url = "http://localhost:8080/theme"
    cookies = {
        "theme": f"{theme}"
    }
    response = requests.get(url=url, cookies=cookies)
    print(response.json())

def main():
    while True:
        print_routes()
        choice = input("\nChoose a Route: ")
        match choice:
            case "0":
                exit()
            case "1":
                call_root()
            case "2":
                call_about()
            case "3":
                call_year()
            case "4":
                call_time()
            case "5":
                call_day()
            case "6":
                call_age_query()
            case "7":
                call_age_path()
            case "8":
                call_age_post()
            case "9":
                call_name_query()
            case "10":
                call_name_path()
            case "11":
                call_headers()
            case "12":
                call_theme()

main()