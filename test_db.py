import sqlite3
import os

def test_database():
    """Test the database connection and operations"""
    DATABASE = 'school_reviews.db'
    
    try:
        # Test connection
        print("Testing database connection...")
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DATABASE)
        print(f"Database path: {db_path}")
        
        connection = sqlite3.connect(db_path)
        print("✓ Database connection successful!")
        
        # Test table creation
        cursor = connection.cursor()
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
        print("✓ Table creation successful!")
        
        # Test insert
        insert_query = """
        INSERT INTO reviews (school_name, reviewer_name, rating, comment)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, ("Test School", "Test User", 5, "This is a test review"))
        connection.commit()
        print("✓ Insert operation successful!")
        
        # Test select
        cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
        reviews = cursor.fetchall()
        print(f"✓ Select operation successful! Found {len(reviews)} reviews")
        
        # Show the reviews
        for review in reviews:
            print(f"  - {review[1]} by {review[2]} (Rating: {review[3]}/5)")
        
        cursor.close()
        connection.close()
        print("✓ All database operations successful!")
        
    except Exception as e:
        print(f"✗ Database test failed: {e}")

if __name__ == "__main__":
    test_database() 