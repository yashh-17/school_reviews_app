from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

# SQLite database file
DATABASE = 'school_reviews.db'

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = sqlite3.connect(DATABASE)
        connection.row_factory = sqlite3.Row  # This enables column access by name
        return connection
    except Exception as e:
        print(f"Error connecting to SQLite: {e}")
        return None

def create_database():
    """Create the database and table if they don't exist"""
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
            print("Database and table created successfully!")
            
    except Exception as e:
        print(f"Error creating database: {e}")

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