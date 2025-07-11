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
        # Ensure the database file path is absolute
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DATABASE)
        print(f"Connecting to database at: {db_path}")
        
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row  # This enables column access by name
        print("Database connection successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to SQLite: {e}")
        return None

def create_database():
    """Create the database and table if they don't exist"""
    try:
        print("Creating database and table...")
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
            cursor.close()
            connection.close()
            print("Database and table created successfully!")
            
            # Verify the table was created
            verify_connection = get_db_connection()
            if verify_connection:
                cursor = verify_connection.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reviews'")
                table_exists = cursor.fetchone()
                cursor.close()
                verify_connection.close()
                
                if table_exists:
                    print("Table verification successful!")
                else:
                    print("Warning: Table verification failed!")
            else:
                print("Warning: Could not verify table creation!")
                
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
        print(f"Attempting to insert review: {school_name}, {reviewer_name}, {rating}")
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
                print("Review inserted successfully!")
                flash('Review submitted successfully!', 'success')
                return redirect(url_for('reviews'))
            except Exception as e:
                print(f"Error inserting review: {e}")
                flash(f'Error submitting review: {e}', 'error')
        else:
            print("Database connection failed!")
            flash('Database connection error!', 'error')
    
    return render_template('add_review.html')

@app.route('/reviews')
def reviews():
    """Display all reviews"""
    print("Fetching reviews from database...")
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
            reviews_list = cursor.fetchall()
            cursor.close()
            connection.close()
            print(f"Successfully fetched {len(reviews_list)} reviews")
            return render_template('reviews.html', reviews=reviews_list)
        except Exception as e:
            print(f"Error fetching reviews: {e}")
            flash(f'Error fetching reviews: {e}', 'error')
            return render_template('reviews.html', reviews=[])
    else:
        print("Database connection failed when fetching reviews!")
        flash('Database connection error!', 'error')
        return render_template('reviews.html', reviews=[])

if __name__ == '__main__':
    # Create database and table on startup
    create_database()
    print("Starting Flask application...")
    app.run(debug=True) 