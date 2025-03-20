import requests

# Define API Endpoints
BASE_URL = "http://127.0.0.1:5000"

AUTH_ENDPOINTS = {
    "login": f"{BASE_URL}/auth/login",
    "register": f"{BASE_URL}/auth/register"
}

LIBRARY_ENDPOINTS = {
    "add_book": f"{BASE_URL}/library/add_book",
    "update_book": f"{BASE_URL}/library/update_book",
    "delete_book": f"{BASE_URL}/library/delete_book",
    "add_category": f"{BASE_URL}/library/add_category",
    "list_books": f"{BASE_URL}/book/books"
}

LENDING_ENDPOINTS = {
    "request_book": f"{BASE_URL}/book_lending/request_book",
    "return_book": f"{BASE_URL}/book_lending/return_book"
}

# Define User Credentials
USER_CREDENTIALS = {
    "librarian": {"username": "librarian_name", "password": "securepass"},
    "user": {"username": "Testing01", "password": "securepass"}
}

# Define Payloads
BOOK_PAYLOADS = {
    "add": {
        "isbn": "978-3-0255-2115",
        "title": "Introduction to Python",
        "category_name": "History",
        "publisher": "MIT Press",
        "language": "English",
        "no_of_copies": 12
    },
    "update": {
        "isbn": "978-3-0255-2115",
        "title": "Introduction to Updated Python",
        "category_name": "History",
        "publisher": "MIT Press",
        "language": "English",
        "no_of_copies": 52
    },
    "delete": {
        "isbn": "978-3-0255-2115"
    }
}

CATEGORY_PAYLOAD = {"category": "Verification"}

BOOK_LENDING_PAYLOADS = {
    "request": {"username": "Testing01", "title": "The Great Adventure"},
    "return": {"username": "Testing01", "title": "The Great Adventure"}
}


# Function to get access token
def get_access_token(user_type):
    """
    Retrieves the access token for a given user type (librarian or user).
    """
    response = requests.post(AUTH_ENDPOINTS["login"], json=USER_CREDENTIALS[user_type])
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Error: Could not get token for {user_type}. Response: {response.json()}")
        return None


# Function to send HTTP requests
def send_request(method, url, payload, headers):
    """
    Generic function to send requests and handle errors.
    """
    response = requests.request(method, url, json=payload, headers=headers)
    return response.json()


# Main test function
def test_api():
    # Get access tokens
    librarian_token = get_access_token("librarian")
    user_token = get_access_token("user")

    if not librarian_token or not user_token:
        print("Failed to retrieve one or more tokens. Exiting test.")
        return

    librarian_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {librarian_token}"}
    user_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {user_token}"}

    print("\n=== Running API Tests for Librarian =================================================")

    # Librarian Actions
    print("Adding Book:", send_request("POST", LIBRARY_ENDPOINTS["add_book"], BOOK_PAYLOADS["add"], librarian_headers))
    print("Updating Book:", send_request("POST", LIBRARY_ENDPOINTS["update_book"], BOOK_PAYLOADS["update"], librarian_headers))
    print("Deleting Book:", send_request("POST", LIBRARY_ENDPOINTS["delete_book"], BOOK_PAYLOADS["delete"], librarian_headers))
    print("Adding Category:", send_request("POST", LIBRARY_ENDPOINTS["add_category"], CATEGORY_PAYLOAD, librarian_headers))

    print("\n=== Running API Tests for User ========================================================")

    # User Actions
    print("Requesting Book:", send_request("POST", LENDING_ENDPOINTS["request_book"], BOOK_LENDING_PAYLOADS["request"], user_headers))
    print("Returning Book:", send_request("POST", LENDING_ENDPOINTS["return_book"], BOOK_LENDING_PAYLOADS["return"], user_headers))

    print("\n==========================================================================================")
    print("Listing Books:", send_request("POST", LIBRARY_ENDPOINTS["list_books"], {}, librarian_headers))


# Run the tests
if __name__ == "__main__":
    test_api()
