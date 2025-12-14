# db.py
import pymysql
from config import Config

def get_db_connection():
    """Create and return a database connection using pymysql"""
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE,
        port=Config.MYSQL_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )