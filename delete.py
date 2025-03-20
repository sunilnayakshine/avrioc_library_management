import requests

login_url = "http://127.0.0.1:5000/auth/login"
register_url = "http://127.0.0.1:5000/auth/register"


book_delete_url = "http://127.0.0.1:5000/library/delete_book"
book_update_url = "http://127.0.0.1:5000/library/update_book"
book_add_url = "http://127.0.0.1:5000/library/add_book"

cat_add_url = "http://127.0.0.1:5000/library/add_category"

book_request_url = "http://127.0.0.1:5000/book_lending/request_book"
book_return_url = "http://127.0.0.1:5000/book_lending/return_book"

list_book_url = "http://127.0.0.1:5000/library/list_all_book"
list_book_by_con_url = "http://127.0.0.1:5000/book/books"

register_payload = {
    "username": "Testing01",
    "password": "securepass",
    "email" : "email",
    "phone": 810566,
    "street_address" : "street",
    "state" : "state",
    "country" : "country",
    "city": "city"
}

login_payload = {
    "username": "librarian_name",
    "password": "securepass"
}

book_add_payload = {
    "isbn": "978-3-16-2025",
    "title": "Introduction to Python",
    "category_name": "History",
    "publisher": "MIT Press",
    "language": "English",
    "no_of_copies": 12
}
book_update_payload = {
    "isbn": "978-3-16-2025",
    "title": "Introduction to Updated",
    "category_name": "History",
    "publisher": "MIT Press",
    "language": "English",
    "no_of_copies": 52
}

list_book_condition_payload = {
    # "title": "The Republic",
    "publisher": "MIT Press"
}

update_book_payload = {
    "isbn": "978-3-16-148410-0",
    "title": "Introduction to Python C#",
    "category_name": "History",
    "publisher": "MIT Press",
    "no_of_copies": 12
}

delete_book_payload = {
    "isbn": "978-3-16-148410-0"
}

cat_add_payload = {
    "category": "category"
}

book_request_payload = {
    "title": "The Great Adventure"
}

book_return_payload = {
    "title": "The Great Adventure"
}

# response = requests.post(register_url, json=register_payload)
response = requests.post(login_url, json=login_payload)
print(response)
access_token = response.json()["access_token"]


headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {access_token}"
           }

response = requests.post(book_delete_url, json=delete_book_payload, headers=headers)

# response = requests.post(book_add_url, json=book_add_payload, headers=headers)
# response = requests.post(book_update_url, json=update_book_payload, headers=headers)
# response = requests.post(cat_add_url, json=cat_add_payload, headers=headers)

# response = requests.post(list_book_by_con_url, json=list_book_condition_payload,  headers=headers)
# response = requests.post(book_request_url, json=book_request_payload, headers=headers)
# response = requests.post(book_return_url, json=book_return_payload, headers=headers)

print(response.json())