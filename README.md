
  

# Library Management API

  

## Overview

  

The Library Management API allows users to manage books, categories, and lending records. This API provides authentication using JWT tokens and includes features for adding, updating, deleting, and retrieving books and categories.

  

## Features

  

- Add, update, and delete books (Requires librarian credentials)

- Add categories

- Borrow and return books

- List books with optional filters (title, category, publisher)

- Authentication with JWT

  

## Installation

  

### Prerequisites

  

- Python

- Flask

- Flask-JWT-Extended

- Flask SQLAlchemy

- PostgreSQL or SQLite

- Requests (for API testing)

### Assumptions :
- Assuming that already librarian is updated in Database and mapped to user.



 

### Setup Instructions

  

1. Clone the repository:

```sh

git clone https://github.com/sunilnayakshine/avrioc_library_management.git

cd avrioc_library_management

```

2. Create and activate a virtual environment:

```sh

python -m venv venv

source venv/bin/activate

```

3. Install dependencies:

```sh

pip install -r requirements.txt

```

4. Set up the database:

```sh

flask db upgrade

```

5. Run the Flask application:

```sh

flask run --debug

```

  

## API Endpoints

  

### Authentication

  

### 1. "Register (For the first time)"

**Endpoint:**  `POST /auth/legister`  **Request Body:**

  

```json

{

"username": "Testing01",

"password": "securepass",

"email" : "email",

"phone": 810566456,

"street_address" : "street",

"state" : "state",

"country" : "country",

"city": "city"

}

```

  

**Response:**

  

```json

{

"Info": "username created succefully"

}
```


#### 1. **Login (Get JWT Token)**

  

**Endpoint:**  `POST /auth/login`  **Request Body:**

  

```json

{

"username": "librarian_name",

"password": "securepass"

}
```

**Response:**

  

```json
{
"access_token": "access-key"
}
```

  
  

### Book Management

  

#### 2. **Add Book**

  

**Endpoint:**  `POST /library/add_book`  **Headers:**  `{Authorization: Bearer <token>}`  **Request Body:**

  

```json
{
	"isbn": "978-3-16-2025",
	"title": "Introduction to Python",
	"category_name": "History",
	"publisher": "MIT Press",
	"language": "English",
	"no_of_copies": 12
}
```

  

**Response:**

  
```json

{"message": "Book added successfully"}

```

  

#### 3. **Update Book**

  

**Endpoint:**  `POST /library/update_book`  **Headers:**  `{Authorization: Bearer <token>}`  **Request Body:**

  

```json
{
"title": "Updated Title",
"publisher": "Updated Publisher"
}
```

  

**Response:**

  

```json

{"message": "Book updated successfully"}

```

  

#### 4. **Delete Book**

  

**Endpoint:**  `POST /library/delete_book`  **Headers:**  `{Authorization: Bearer <token>}`  **Request Body:**

  

```json

{

"isbn": "9783025521156"

}
```

**Response:**

  

```json

{"message": "Book deleted successfully"}

  

```

  

### Add Category

  

**Endpoint:**  `POST /library/add_category`  **Headers:**  `{Authorization: Bearer <token>}`  **Request Body:**

  

**Response:**

  

```json

{"category name": "testing interview", "message": "Category added successfully"}

```

  

### Book Retrieval

  

#### 5. **List Books**

  

**Endpoint:**  `POST /book/books`  **Headers:**  `{Authorization: Bearer <token>}`  **Request Body (Optional Filters):**

  

```json

{

"title": "Book Title",

"category_name": "Fiction",

"publisher": "XYZ Publishers"

}

  

```

  

**Response:**

  

```json

[

	{

	"title": "Book Title",
	"isbn": "9783025521156",
	"category_name": "Fiction",
	"publisher": "XYZ Publishers",
	"author": "John Doe",
	"no_of_copies": 2023
	}
]

  

```

  

### Borrowing & Returning Books

  

#### 6. **Request Book (Borrow)**

  

**Endpoint:**  `POST /book_lending/request`  **Request Body:**

  

```json

{
"title": "The Great Adventure"
}

```

  

**Response:**

  
```json

{
	"due_date": "Fri, 04 Apr 2025 00:00:00 GMT",
	"message": "Book borrowed successfully"
}
```

  

#### 7. **Return Book**

  

**Endpoint:**  `POST /book_lending/return`  **Request Body:**

  

```json

{
"title": "The Great Adventure"
}

  

```

  

**Response:**

  

```json

{

"message": "Lending record deleted and logged in reservation history"

}

```

  

## Debugging & Logs

  

If you encounter an issue, check the logs:

  

```sh

flask  run  --debug

```

### Simulation API functionality:

Please use the docker-compose to start the application. docker-compose will start the database and followed by flask app. Please make sure run the `test/auth_api.py` first, because this will add the librarian first. For simplicity first user is made as librarian.

To verify the functionlity, please adjust the files in `test` folder. 

To start the application:

```
cd avrioc_library_management
docker-compose up
```


To test the functionality:

```
python test/auth_api.py
python test/library_api.py
python test/reservation_api.py

```