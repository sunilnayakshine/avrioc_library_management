import requests

book_add_payloads = {
        "isbn": "978-3-16-2025",
        "title": "Added new book",
        "category_name": "Science",
        "publisher": "new Press",
        "language": "New language",
        "no_of_copies": 123
    }

book_update_payload =     {
        "isbn": "978-3-16-2025",
        "title": "Updated book name",
    }

book_delete_payload = {
        "isbn" : "978-3-16-2025"  
    }

book_get_payload = {
    "title" : "Updated book name"
}

url = "http://127.0.0.1:5000/auth/login"
def login_user(username="librarian", password="mypassword"):
    response = requests.post(url, json={"username": username, "password": password})
    return response.json()

librarian_headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {login_user()['access_token']}"
           }

user_headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {login_user('new register', 'register')['access_token']}"
           }

def add_book_by_librarian():
    response = requests.post(url="http://127.0.0.1:5000/library/add_book", json=book_add_payloads, headers=librarian_headers)
    return response.json()
    
def update_book_by_librarian():
    response = requests.post(url="http://127.0.0.1:5000/library/update_book", json=book_update_payload, headers=librarian_headers)
    return response.json()

def delete_book_by_librarian():
    response = requests.post(url="http://127.0.0.1:5000/library/delete_book", json=book_delete_payload, headers=librarian_headers)
    return response.json()

def add_book_by_user():
    response = requests.post(url="http://127.0.0.1:5000/library/add_book", json=book_add_payloads, headers=user_headers)
    return response.json()

def get_book_by_title(payload):
    response = requests.post(url="http://127.0.0.1:5000/book/books", json=payload, headers=librarian_headers)
    return response.json()
    
def update_book_by_user():
    response = requests.post(url="http://127.0.0.1:5000/library/update_book", json=book_update_payload, headers=user_headers)
    return response.json()

def delete_book_by_user():
    response = requests.post(url="http://127.0.0.1:5000/library/delete_book", json=book_delete_payload, headers=user_headers)
    return response.json()

print("\n============== Library management by Librarian ===============")
print(add_book_by_librarian())
print(get_book_by_title({"title": "Added new book"}))
# print(update_book_by_librarian())
# print(get_book_by_title({"title": "Updated book name"}))
# print(delete_book_by_librarian()) # 

print("\n============== Library management by User  ====================")
print(add_book_by_user())
print(update_book_by_user())
print(delete_book_by_user())

