from database import db

class Address(db.Model):
    __tablename__ = 'address'
    address_id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    phone = db.Column(db.String)

    accounts = db.relationship("Account", back_populates="address")

class Account(db.Model):
    __tablename__ = 'account'
    account_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    username = db.Column(db.String)
    address_id = db.Column(db.Integer, db.ForeignKey('address.address_id'))
    email = db.Column(db.String)

    address = db.relationship("Address", back_populates="accounts")
    book_lendings = db.relationship("BookLending", back_populates="account")
    reservations = db.relationship("BookReservation", back_populates="account")
    reservation_histories = db.relationship("ReservationHistory", back_populates="account")
    librarian = db.relationship("Librarian", back_populates="account", uselist=False)
    library_card = db.relationship("LibraryCard", back_populates="account", uselist=False)
    
class LibraryCard(db.Model):
    __tablename__ = 'librarycard'
    card_number = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    issued_date = db.Column(db.Date)
    active = db.Column(db.Boolean)
    expiry_date = db.Column(db.Date)

    account = db.relationship("Account", back_populates="library_card")

class Librarian(db.Model):
    __tablename__ = 'librarian'
    librarian_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))

    account = db.relationship("Account", back_populates="librarian")

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    books = db.relationship("Book", back_populates="category")

class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    publisher = db.Column(db.String)
    language = db.Column(db.String)
    no_of_copies = db.Column(db.Integer)

    category = db.relationship("Category", back_populates="books")
    book_lendings = db.relationship("BookLending", back_populates="book")
    reservations = db.relationship("BookReservation", back_populates="book")
    reservation_histories = db.relationship("ReservationHistory", back_populates="book")
    
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "category_id": self.category_id,
            "publisher": self.publisher,
            "language": self.language,
            "no_of_copies": self.no_of_copies
        }

class BookLending(db.Model):
    __tablename__ = 'booklending'
    lending_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    creation_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    isbn = db.Column(db.String, db.ForeignKey('book.isbn'))

    account = db.relationship("Account", back_populates="book_lendings")
    book = db.relationship("Book", back_populates="book_lendings")

class BookReservation(db.Model):
    __tablename__ = 'bookreservation'
    reservation_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    creation_date = db.Column(db.Date)
    isbn = db.Column(db.String, db.ForeignKey('book.isbn'))

    account = db.relationship("Account", back_populates="reservations")
    book = db.relationship("Book", back_populates="reservations")

class ReservationHistory(db.Model):
    __tablename__ = 'reservation_history'
    history_id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'))
    borrowed_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    isbn = db.Column(db.String, db.ForeignKey('book.isbn'))

    account = db.relationship("Account", back_populates="reservation_histories")
    book = db.relationship("Book", back_populates="reservation_histories")
    
    def to_dict(self):
        return {
            "history_id": self.history_id,
            "account_id": self.account_id,
            "borrowed_date": str(self.borrowed_date),
            "return_date": str(self.return_date) if self.return_date else None,
            "isbn": self.isbn
        }