from DAO.book_dao import BookDAO


class BookService:
    @staticmethod
    def fetch_books(title=None, category_name=None, publisher=None):
        books = BookDAO.get_books_by_filter(title, category_name, publisher)
        return [book.to_dict() for book in books] if books else []
