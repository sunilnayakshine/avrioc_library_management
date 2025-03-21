
import requests


register_librarian_payload = {
            "username": "librarian",
            "password": "mypassword",
            "email" : "librarian@email.com",
            "phone": 123564,
            "street_address" : "librarian street",
            "state" : "librarian state",
            "country" : "librarian country",
            "city": "librarian city"
    }
register_user_payload = {
            "username": "new register",
            "password": "register",
            "email" : "register@email.com",
            "phone": 123564,
            "street_address" : "new street_address",
            "state" : "new state",
            "country" : "new country",
            "city": "new city"
    }


url = "http://127.0.0.1:5000/auth/register"

def register_librarian():
    response = requests.post(url, json=register_librarian_payload)
    print(response.json())
    return response

def register_user():
    response = requests.post(url, json=register_user_payload)
    print(response.json())
    return response

print("\n========== Register user ====================================")
register_librarian()
register_user()
