from DAO.book_lending_dao import BookLendingDAO
from DAO.book_dao import BookDAO
from DAO.user_dao import UserDAO
from datetime import date, timedelta
from database import db


class BookLendingService:
    @staticmethod
    def request_book(username, title):
        try:
            book = BookDAO.get_book_by_title(title)
            account_id = UserDAO.get_account_id_by_username(username)
            if not book:
                raise ValueError("Book not found")

            active_lendings = BookLendingDAO.get_active_lendings(account_id, book.isbn)
            if active_lendings:
                raise ValueError("You have already borrowed this book")

            if book.no_of_copies <= 0:
                available_date = BookLendingDAO.add_reservation(account_id=account_id, isbn=book.isbn)
                raise ValueError("Book is currently out of stock: ", available_date)

            due_date = date.today() + timedelta(days=14)
            BookLendingDAO.add_lending(account_id, book.isbn, due_date)

            book.no_of_copies -= 1
            db.session.commit()

            return {"message": "Book borrowed successfully", "due_date": due_date}
        except ValueError as e:
            return {"error": str(e)}, 400
