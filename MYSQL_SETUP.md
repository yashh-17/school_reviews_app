# MySQL Setup Guide

## Option 1: Use SQLite (Easier)
If you want to get started quickly, use the SQLite version:
```bash
python app_sqlite.py
```

## Option 2: Setup MySQL

### Step 1: Install MySQL Server
1. Download MySQL Server from: https://dev.mysql.com/downloads/mysql/
2. Install with default settings
3. Remember the root password you set during installation

### Step 2: Update Database Configuration
Edit `app.py` and update the DB_CONFIG:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password_here',  # Replace with your actual password
    'database': 'school_reviews'
}
```

### Step 3: Alternative - Create New MySQL User
If you don't want to use root, create a new user:

1. Open MySQL Command Line Client
2. Login with root password
3. Run these commands:

```sql
CREATE USER 'schooluser'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON school_reviews.* TO 'schooluser'@'localhost';
FLUSH PRIVILEGES;
```

Then update `app.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'schooluser',
    'password': 'your_password',
    'database': 'school_reviews'
}
```

### Step 4: Run the Application
```bash
python app.py
```

## Troubleshooting

### "Access denied for user 'root'@'localhost'"
- Make sure MySQL server is running
- Check that the password in `app.py` matches your MySQL root password
- Try creating a new user as shown above

### "Can't connect to MySQL server"
- Ensure MySQL service is running
- Check if MySQL is installed correctly
- Try restarting MySQL service

### Port Issues
If port 5000 is busy, change the port in `app.py`:
```python
app.run(debug=True, port=5001)
``` 