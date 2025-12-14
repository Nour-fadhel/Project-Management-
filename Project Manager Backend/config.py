import os
from datetime import timedelta



class Config:
    SECRET_KEY = "your_secret_key_here"
    JWT_SECRET_KEY = "your_jwt_secret_key_here"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)

    # MySQL Configuration
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"  # Your MySQL password
    MYSQL_DATABASE = "projectmanager_db"

    # SQLAlchemy URI - IMPORTANT: Note the 'f' prefix before the quote!
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    #                         ↑ THIS 'f' IS CRITICAL - it makes it an f-string!

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Frontend
    FRONTEND_URL = 'http://localhost:5173'

    # Gmail Configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tounaktisafa3@gmail.com'
    MAIL_PASSWORD = 'aifa jnxm vhwj tbsu'  # Gmail App Password
    MAIL_DEFAULT_SENDER = 'tounaktisafa3@gmail.com'