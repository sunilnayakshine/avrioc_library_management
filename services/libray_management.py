from database import db
from DAO.book_dao import BookDAO
from models import Category, Book, BookReservation
from sqlalchemy.exc import IntegrityError


class LibraryService:

    @staticmethod
    def add_category(name):
        """Add a new category if it does not exist."""
        try:
            existing_category = db.session.query(Category).filter_by(name=name).first()
            if existing_category:
                return {"message": "Category already exists", "category_id": existing_category.name}, 200

            new_category = Category(name=name)
            db.session.add(new_category)
            db.session.commit()
            return {"message": "Category added successfully", "category name": new_category.name}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def add_book(isbn, title, category_name, publisher, language, no_of_copies):
        """Add a new book after checking if the category exists."""
        try:
            category = db.session.query(Category).filter_by(name=category_name).first()
            
            existing_book = db.session.query(Book).filter_by(isbn=isbn).first()
            if existing_book:
                return {"error": f"Book with ISBN '{isbn}' already exists"}, 400

            category = db.session.query(Category).filter_by(name=category_name).first()
            if not category:
                return {"error": f"Category '{category_name}' not found"}, 400

            new_book = Book(
                isbn=isbn,
                title=title,
                category_id=category.id,
                publisher=publisher,
                language=language,
                no_of_copies=no_of_copies
            )

            db.session.add(new_book)
            db.session.commit()
            return {"message": "Book added successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_book(isbn):
        """Delete a book from the database by ISBN."""
        try:
            book = db.session.query(Book).filter_by(isbn=isbn).first()
            if not book:
                return {"error": "Book not found"}, 404
            
            db.session.query(BookReservation).filter_by(isbn=isbn).delete() ## Need to send notification
            db.session.delete(book)
            db.session.commit()
            return {"message": "Book deleted successfully"}, 200
        except IntegrityError:
            db.session.rollback()
            return {"error": "Book is lended to user, so can't be deleted."}, 500
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def update_book(isbn, title=None, category_name=None, publisher=None, language=None, no_of_copies=None):
        """Update book details, ensuring category exists before assigning."""
        try:
            book = db.session.query(Book).filter_by(isbn=isbn).first()
            if not book:
                return {"error": "Book not found"}, 404

            if title:
                book.title = title
            if category_name:
                category = db.session.query(Category).filter_by(name=category_name).first()
                if not category:
                    return {"error": f"Category '{category_name}' not found"}, 400
                book.category_id = category.id
            if publisher:
                book.publisher = publisher
            if language:
                book.language = language
            if no_of_copies is not None:
                book.no_of_copies = no_of_copies

            db.session.add(book)
            db.session.commit()

            return {"message": "Book updated successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
