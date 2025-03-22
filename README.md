
  

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

### Sample run:


**Application Setup:**
Cloning the source and starting the database and flask app.
```
[sunil@myserver testing_api]$ git clone https://github.com/sunilnayakshine/avrioc_library_management.git
Cloning into 'avrioc_library_management'...
remote: Enumerating objects: 62, done.
remote: Counting objects: 100% (62/62), done.
remote: Compressing objects: 100% (48/48), done.
remote: Total 62 (delta 15), reused 57 (delta 10), pack-reused 0 (from 0)
Unpacking objects: 100% (62/62), done.
[sunil@myserver testing_api]$ cd avrioc_library_management/
[sunil@myserver avrioc_library_management]$
[sunil@myserver avrioc_library_management]$ docker-compose up -d --build
[+] Building 2.1s (17/17) FINISHED                                                                                                                                            docker:default
 => [postgres internal] load .dockerignore                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [postgres internal] load build definition from Dockerfile.database                                                                                                                  0.0s
 => => transferring dockerfile: 231B                                                                                                                                                    0.0s
 => [postgres internal] load metadata for docker.io/library/postgres:latest                                                                                                             0.8s
 => [postgres internal] load build context                                                                                                                                              0.0s
 => => transferring context: 1.96kB                                                                                                                                                     0.0s
 => [postgres 1/2] FROM docker.io/library/postgres:latest@sha256:7f29c02ba9eeff4de9a9f414d803faa0e6fe5e8d15ebe217e3e418c82e652b35                                                       0.0s
 => CACHED [postgres 2/2] COPY db.sql /docker-entrypoint-initdb.d/db.sql                                                                                                                0.0s
 => [postgres] exporting to image                                                                                                                                                       0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:729fc82e4fd39c09f3b701c9ee2ae06ece81247bbbf395dd1a5d1ee164de5505                                                                                            0.0s
 => => naming to docker.io/library/avrioc_library_management-postgres                                                                                                                   0.0s
 => [flask-app internal] load .dockerignore                                                                                                                                             0.0s
 => => transferring context: 2B                                                                                                                                                         0.0s
 => [flask-app internal] load build definition from Dockerfile.flask                                                                                                                    0.0s
 => => transferring dockerfile: 292B                                                                                                                                                    0.0s
 => [flask-app internal] load metadata for docker.io/library/python:3.9                                                                                                                 0.9s
 => [flask-app 1/5] FROM docker.io/library/python:3.9@sha256:bc2e05bca883473050fc3b7c134c28ab822be73126ba1ce29517d9e8b7f3703b                                                           0.0s
 => [flask-app internal] load build context                                                                                                                                             0.0s
 => => transferring context: 94.51kB                                                                                                                                                    0.0s
 => CACHED [flask-app 2/5] WORKDIR /app                                                                                                                                                 0.0s
 => CACHED [flask-app 3/5] COPY requirements.txt .                                                                                                                                      0.0s
 => CACHED [flask-app 4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                           0.0s
 => [flask-app 5/5] COPY . .                                                                                                                                                            0.1s
 => [flask-app] exporting to image                                                                                                                                                      0.0s
 => => exporting layers                                                                                                                                                                 0.0s
 => => writing image sha256:528ee05844c4593100bea56b261107d368585d9c1155d1683a3ebd2ac853ba63                                                                                            0.0s
 => => naming to docker.io/library/avrioc_library_management-flask-app                                                                                                                  0.0s
[+] Running 2/3
 ⠙ Network avrioc_library_management_default  Created                                                                                                                                  11.1s
 ✔ Container postgres-db                      Healthy                                                                                                                                  10.8s
 ✔ Container flask-app                        Started                                                                                                                                  11.0s
[sunil@myserver avrioc_library_management]$

```

**To setup librarian and test functionality of API's:**

```
[sunil@myserver avrioc_library_management]$ docker exec -it postgres-db  psql -h 127.0.0.1 -p 5432 -U sunil -d library -c "select * from librarian;"
 librarian_id | account_id
--------------+------------
            1 |          1
(1 row)

[sunil@myserver avrioc_library_management]$ docker exec -it postgres-db  psql -h 127.0.0.1 -p 5432 -U sunil -d library -c "select * from category;"
 id |    name
----+-------------
  1 | Fiction
  2 | Non-Fiction
  3 | Science
  4 | History
  5 | Biography
(5 rows)

[sunil@myserver avrioc_library_management]$ docker exec -it flask-app bash -c "python test_api/auth_api.py"

========== Register user ====================================
{'Info': 'username created succefully'}
{'Info': 'username created succefully'}
[sunil@myserver avrioc_library_management]$ docker exec -it flask-app bash -c "python test_api/library_api.py"

============== Library management by Librarian ===============
{'message': 'Book added successfully'}
[{'category_id': 3, 'isbn': '978-3-16-2025', 'language': 'New language', 'no_of_copies': 123, 'publisher': 'new Press', 'title': 'Added new book'}]

============== Library management by User  ====================
{'error': 'Unauthorized access'}
{'error': 'Unauthorized access'}
{'error': 'Unauthorized access'}
[sunil@myserver avrioc_library_management]$ docker exec -it flask-app bash -c "python test_api/reservation_api.py"
{'due_date': 'Sat, 05 Apr 2025 00:00:00 GMT', 'message': 'Book borrowed successfully'}
{'message': 'Lending record deleted and logged in reservation history'}
[sunil@myserver avrioc_library_management]$

```