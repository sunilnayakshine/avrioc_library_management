class Config:

    library_db = {
        "database": "pub_test",
        "user": "postgres",
        "password": "Sunil@123",
        "host": "localhost",
        "port": "5432",
    }
    SECRET_KEY = "super-secret-key"
    JWT_SECRET_KEY = "jwt-secret-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Sunil%40123@localhost:5432/pub_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()
