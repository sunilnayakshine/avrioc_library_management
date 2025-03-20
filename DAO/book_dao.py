from models import Book, Category
from database import db


class BookDAO:
    @staticmethod
    def get_books_by_filter(title=None, category_name=None, publisher=None):
        category_id = db.session.query(Category).filter_by(name=category_name).first()
        query = db.session.query(Book).join(Category, Book.category_id == Category.id)

        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))
        if category_name:
            query = query.filter(Book.category_id == category_id)
        if publisher:
            query = query.filter(Book.publisher.ilike(f"%{publisher}%"))

        return query.all()

    @staticmethod
    def get_book_by_title(title):
        return Book.query.filter_by(title=title).first()
        
    