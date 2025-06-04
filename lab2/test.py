import unittest
import requests
from datetime import datetime

class TestCases(unittest.TestCase):
    def test_getRoot(self):
        url = "http://localhost:8080/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Lab 1!",
        })

    def test_getAbout(self):
        url = "http://localhost:8080/about/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "This is my FastAPI service!",
        })

    def test_getYear(self):
        url = "http://localhost:8080/year/"
        response = requests.get(url)

        expected_year = datetime.now().year

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": f"The year is now {expected_year}!",
        })

    def test_getTime(self):
        url = "http://localhost:8080/time/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)


    def test_getDay(self):
        url = "http://localhost:8080/day/"
        response = requests.get(url)

        expected_day = datetime.now().strftime("%A")

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": f"The day is now {expected_day}!",
        })

    def test_getAge(self):
        url = "http://localhost:8080/age?birth_year=2003&current_year=2025"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "You are 22 years old!",
        })

    def test_getAgePath(self):
        url = "http://localhost:8080/age/2003/2025"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "You are 22 years old!",
        })

    def test_getPerson(self):
        url = "http://localhost:8080/person"
        data = {
            "name": "Denis",
            "birth_year": 2003,
            "current_year": 2025,
        }
        response = requests.post(url, json=data)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Denis, You are 22 years old!",
        })

    def test_getName(self):
        url = "http://localhost:8080/name?names=Denis"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Denis!",
        })

    def test_getNamePath(self):
        url = "http://localhost:8080/name/Denis"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Denis!",
        })

    def test_getHeaders(self):
        url = "http://localhost:8080/headers/"
        headers = {
            "Content-Type": "application/json",
            "X-Custom-Header": "CustomValue",
            "user-email": "demo@example.com",
            "user-role": "admin",
            "device-type": "desktop"
        }
        response = requests.get(url=url, headers=headers)

        print("Status code:", response.status_code)
        print("Response Body:", response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "user-email": "demo@example.com",
            "user-role": "admin",
            "device-type": "desktop"
        })

    def test_getTheme(self):
        url = "http://localhost:8080/theme/"
        cookies = {
            "theme": "dark"
        }
        response = requests.get(url=url, cookies=cookies)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"theme": "dark"})