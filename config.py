import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE') or 'school_reviews'
    SQLITE_DATABASE = os.environ.get('SQLITE_DATABASE') or 'school_reviews.db'
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE') or 'sqlite' 