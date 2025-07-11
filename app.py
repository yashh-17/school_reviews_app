from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import sqlite3
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Database configuration
DB_CONFIG = {
    'host': app.config['MYSQL_HOST'],
    'user': app.config['MYSQL_USER'],
    'password': app.config['MYSQL_PASSWORD'],
    'database': app.config['MYSQL_DATABASE']
}

def get_db_connection():
    """Create and return a database connection"""
    if app.config['DATABASE_TYPE'] == 'mysql':
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
    else:
        # SQLite fallback
        try:
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), app.config['SQLITE_DATABASE'])
            connection = sqlite3.connect(db_path)
            connection.row_factory = sqlite3.Row
            return connection
        except Exception as e:
            print(f"Error connecting to SQLite: {e}")
            return None

def create_database():
    """Create the database and table if they don't exist"""
    if app.config['DATABASE_TYPE'] == 'mysql':
        try:
            # Connect without specifying database
            connection = mysql.connector.connect(
                host=DB_CONFIG['host'],
                user=DB_CONFIG['user'],
                password=DB_CONFIG['password']
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                
                # Create database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS school_reviews")
                cursor.execute("USE school_reviews")
                
                # Create table if it doesn't exist
                create_table_query = """
                CREATE TABLE IF NOT EXISTS reviews (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    school_name VARCHAR(100),
                    reviewer_name VARCHAR(100),
                    rating INT,
                    comment TEXT
                )
                """
                cursor.execute(create_table_query)
                connection.commit()
                
                cursor.close()
                connection.close()
                print("MySQL Database and table created successfully!")
                
        except Error as e:
            print(f"Error creating MySQL database: {e}")
    else:
        # SQLite database creation
        try:
            connection = get_db_connection()
            if connection:
                cursor = connection.cursor()
                
                # Create table if it doesn't exist
                create_table_query = """
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    school_name TEXT NOT NULL,
                    reviewer_name TEXT NOT NULL,
                    rating INTEGER NOT NULL,
                    comment TEXT NOT NULL
                )
                """
                cursor.execute(create_table_query)
                connection.commit()
                connection.close()
                print("SQLite Database and table created successfully!")
                
        except Exception as e:
            print(f"Error creating SQLite database: {e}")

@app.route('/')
def index():
    """Redirect to reviews page"""
    return redirect(url_for('reviews'))

@app.route('/addreview', methods=['GET', 'POST'])
def add_review():
    """Handle adding new reviews"""
    if request.method == 'POST':
        school_name = request.form['school_name']
        reviewer_name = request.form['reviewer_name']
        rating = request.form['rating']
        comment = request.form['comment']
        
        # Validate input
        if not school_name or not reviewer_name or not rating or not comment:
            flash('All fields are required!', 'error')
            return render_template('add_review.html')
        
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                flash('Rating must be between 1 and 5!', 'error')
                return render_template('add_review.html')
        except ValueError:
            flash('Rating must be a number!', 'error')
            return render_template('add_review.html')
        
        # Insert into database
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                
                if app.config['DATABASE_TYPE'] == 'mysql':
                    insert_query = """
                    INSERT INTO reviews (school_name, reviewer_name, rating, comment)
                    VALUES (%s, %s, %s, %s)
                    """
                else:
                    insert_query = """
                    INSERT INTO reviews (school_name, reviewer_name, rating, comment)
                    VALUES (?, ?, ?, ?)
                    """
                
                cursor.execute(insert_query, (school_name, reviewer_name, rating, comment))
                connection.commit()
                cursor.close()
                connection.close()
                flash('Review submitted successfully!', 'success')
                return redirect(url_for('reviews'))
            except Exception as e:
                flash(f'Error submitting review: {e}', 'error')
        else:
            flash('Database connection error!', 'error')
    
    return render_template('add_review.html')

@app.route('/reviews')
def reviews():
    """Display all reviews"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            if app.config['DATABASE_TYPE'] == 'mysql':
                cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
            else:
                cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
            
            reviews_list = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template('reviews.html', reviews=reviews_list)
        except Exception as e:
            flash(f'Error fetching reviews: {e}', 'error')
            return render_template('reviews.html', reviews=[])
    else:
        flash('Database connection error!', 'error')
        return render_template('reviews.html', reviews=[])

if __name__ == '__main__':
    # Create database and table on startup
    create_database()
    app.run(debug=True) 