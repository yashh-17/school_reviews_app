from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database setup
DATABASE = 'school_reviews.db'

def init_db():
    """Initialize the database"""
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DATABASE)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_name TEXT NOT NULL,
            reviewer_name TEXT NOT NULL,
            rating INTEGER NOT NULL,
            comment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def get_db():
    """Get database connection"""
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DATABASE)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect(url_for('reviews'))

@app.route('/addreview', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school_name = request.form['school_name']
        reviewer_name = request.form['reviewer_name']
        rating = request.form['rating']
        comment = request.form['comment']
        
        # Validation
        if not all([school_name, reviewer_name, rating, comment]):
            flash('All fields are required!', 'error')
            return render_template('add_review.html')
        
        try:
            rating = int(rating)
            if not 1 <= rating <= 5:
                flash('Rating must be between 1 and 5!', 'error')
                return render_template('add_review.html')
        except ValueError:
            flash('Rating must be a number!', 'error')
            return render_template('add_review.html')
        
        # Save to database
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (?, ?, ?, ?)',
                (school_name, reviewer_name, rating, comment)
            )
            conn.commit()
            conn.close()
            flash('Review submitted successfully!', 'success')
            return redirect(url_for('reviews'))
        except Exception as e:
            print(f"Database error: {e}")
            flash('Error saving review. Please try again.', 'error')
    
    return render_template('add_review.html')

@app.route('/reviews')
def reviews():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reviews ORDER BY id DESC')
        reviews_list = cursor.fetchall()
        conn.close()
        return render_template('reviews.html', reviews=reviews_list)
    except Exception as e:
        print(f"Error fetching reviews: {e}")
        flash('Error loading reviews.', 'error')
        return render_template('reviews.html', reviews=[])

if __name__ == '__main__':
    init_db()
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000) 