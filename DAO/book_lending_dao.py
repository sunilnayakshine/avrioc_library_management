from models import db, Book, ReservationHistory, BookLending, Account, BookReservation
from datetime import date
from sqlalchemy.sql import func
    

class BookLendingDAO:
    @staticmethod
    def get_active_lendings(account_id, isbn):
        return BookLending.query.filter_by(account_id=account_id, isbn=isbn).all()

    @staticmethod
    def add_lending(account_id, isbn, due_date):
        new_lending = BookLending(account_id=account_id, isbn=isbn, due_date=due_date, creation_date=date.today())
        db.session.add(new_lending)
        db.session.commit()
        return new_lending

    @staticmethod
    def delete_lending(username, book_title):
        lending = (
        BookLending.query
        .join(Account, Account.account_id == BookLending.account_id)
        .join(Book, Book.isbn == BookLending.isbn)
        .filter(Account.username == username, Book.title == book_title)
        .first()
        )

        if lending:
            reservation_history = ReservationHistory(
                account_id=lending.account_id,
                borrowed_date=lending.creation_date,
                return_date=date.today(),
                isbn=lending.isbn
            )
            db.session.add(reservation_history)

            book = Book.query.filter_by(isbn=lending.isbn).first()
            if book:
                book.no_of_copies += 1
            db.session.delete(lending)
            db.session.commit()
            return {"message": "Lending record deleted and logged in reservation history"}
        else:
            return {"message": "Lending record not found"}

    @staticmethod
    def add_reservation(account_id, isbn):

        existing_reservation = db.session.query(BookReservation).filter(
            BookReservation.account_id == account_id,
            BookReservation.isbn == isbn
        ).first()

        if existing_reservation:
            raise ValueError(f"User has already reserved the book (ISBN: {isbn})")

        next_available_date = db.session.query(func.min(BookLending.due_date)).filter(
            BookLending.isbn == isbn,
            BookLending.return_date.is_(None)
        ).scalar()

        new_reservation = BookReservation(
            account_id=account_id,
            isbn=isbn,
            creation_date=func.current_date(),
            status_id=1
        )
        db.session.add(new_reservation)
        db.session.commit()
        return next_available_date
