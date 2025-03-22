import requests

payload = {
    "title": "Added new book"
}

url = "http://127.0.0.1:5000/auth/login"
def login_user(username="new register", password="register"):
    response = requests.post(url, json={"username": username, "password": password})
    return response.json()

headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {login_user()['access_token']}"
           }

def request_book():
    response = requests.post(url="http://127.0.0.1:5000/book_lending/request_book", json=payload, headers=headers)
    return response.json()

def return_book():
    response = requests.post(url="http://127.0.0.1:5000/book_lending/return_book", json=payload, headers=headers)
    return response.json()

print(request_book())
print(return_book())