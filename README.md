
# Library Management API

## Overview

The Library Management API allows users to manage books, categories, and lending records. This API provides authentication using JWT tokens and includes features for adding, updating, deleting, and retrieving books and categories.

## Features

-   Add, update, and delete books (Requires librarian credentials)
-   Add categories
-   Borrow and return books
-   List books with optional filters (title, category, publisher)
-   Authentication with JWT

## Installation

### Prerequisites

-   Python
-   Flask
-   Flask-JWT-Extended
-   Flask SQLAlchemy
-   PostgreSQL or SQLite
-   Requests (for API testing)

### Setup Instructions

1.  Clone the repository:
    
    ```sh
    git clone https://github.com/your-repo/library-api.git
    cd library-api
    
    ```
    
2.  Create and activate a virtual environment:
    
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    
    ```
    
3.  Install dependencies:
    
    ```sh
    pip install -r requirements.txt
    
    ```
    
4.  Set up the database:
    
    ```sh
    flask db upgrade
    
    ```
    
5.  Run the Flask application:
    
    ```sh
    flask run --debug
    
    ```
    

## API Endpoints

### Authentication

#### 1. **Login (Get JWT Token)**

**Endpoint:** `POST /login` **Request Body:**

```json
{
    "username": "librarian_name",
    "password": "securepass"
}

```

**Response:**

```json
{
    "access_token": "your-jwt-token"
}

```

### Book Management

#### 2. **Add Book**

**Endpoint:** `POST /books/add` **Headers:** `{Authorization: Bearer <token>}` **Request Body:**

```json
{
    "title": "Book Title",
    "isbn": "9783025521156",
    "category_name": "Fiction",
    "publisher": "XYZ Publishers",
    "author": "John Doe",
    "publication_year": 2023
}

```

**Response:**

```json
{"message": "Book added successfully"}

```

#### 3. **Update Book**

**Endpoint:** `POST /books/update` **Headers:** `{Authorization: Bearer <token>}` **Request Body:**

```json
{
    "isbn": "9783025521156",
    "title": "Updated Title",
    "publisher": "Updated Publisher"
}

```

**Response:**

```json
{"message": "Book updated successfully"}

```

#### 4. **Delete Book**

**Endpoint:** `DELETE /books/delete` **Headers:** `{Authorization: Bearer <token>}` **Request Body:**

```json
{
    "isbn": "9783025521156"
}

```

**Response:**

```json
{"message": "Book deleted successfully"}

```

### Book Retrieval

#### 5. **List Books**

**Endpoint:** `POST /books` **Headers:** `{Authorization: Bearer <token>}` **Request Body (Optional Filters):**

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
        "publication_year": 2023
    }
]

```

### Borrowing & Returning Books

#### 6. **Request Book (Borrow)**

**Endpoint:** `POST /books/request` **Request Body:**

```json
{
    "isbn": "9783025521156"
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

**Endpoint:** `POST /books/return` **Request Body:**

```json
{
    "isbn": "9783025521156"
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
flask run --debug
```