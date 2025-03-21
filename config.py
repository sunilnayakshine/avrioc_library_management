class Config:

    SECRET_KEY = "super-secret-key"
    JWT_SECRET_KEY = "jwt-secret-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://sunil:mypassword@postgres-db:5432/library"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()
