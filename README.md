# School Reviews Flask Application

A complete Flask web application that allows users to submit and view school reviews using MySQL or SQLite database.

## ✅ **Requirements Met**

### **Core Features:**
- ✅ **Flask Routing & Templating** - Clean route structure with template inheritance
- ✅ **MySQL Database Integration** - Full MySQL support with SQLite fallback
- ✅ **HTML Form Handling** - Complete form validation and processing
- ✅ **Bootstrap Layout** - Modern, responsive UI design
- ✅ **Python Code Structure** - Well-organized, maintainable code

### **Technical Requirements:**
- ✅ **Working Flask app** - Fully functional application
- ✅ **Reviews stored and retrieved from database** - MySQL/SQLite support
- ✅ **Clean UI using Bootstrap** - Modern, responsive design
- ✅ **Form validation** - Comprehensive input validation
- ✅ **Environment variables** - Config.py for database credentials

## 📁 **Project Structure**

```
school_reviews_app/
├── app.py                 # Main Flask application
├── config.py              # Database configuration
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── env_example.txt       # Environment variables example
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── add_review.html   # Add review form
│   └── reviews.html      # Display all reviews
└── static/               # Static files (CSS, JS, images)
```

## 🛠️ **Tech Stack Used**

- **Flask** - Web framework
- **MySQL** - Primary database (with SQLite fallback)
- **Jinja2 Templates** - Template engine
- **Bootstrap** - UI framework
- **Python-dotenv** - Environment variable management

## 🚀 **Quick Start**

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Configure Database**
Copy `env_example.txt` to `.env` and configure:
```bash
# For SQLite (default)
DATABASE_TYPE=sqlite

# For MySQL
DATABASE_TYPE=mysql
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=school_reviews
```

### **3. Run the Application**
```bash
python app.py
```

### **4. Access the Application**
- **URL:** `http://127.0.0.1:5000`
- **Add Reviews:** `/addreview`
- **View Reviews:** `/reviews`

## 📋 **Routes Implemented**

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Redirects to reviews page |
| `/addreview` | GET/POST | Display form and handle review submission |
| `/reviews` | GET | Display all reviews in table format |

## 🗄️ **Database Schema**

### **MySQL Table:**
```sql
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100),
    reviewer_name VARCHAR(100),
    rating INT,
    comment TEXT
);
```

### **SQLite Table:**
```sql
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_name TEXT NOT NULL,
    reviewer_name TEXT NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT NOT NULL
);
```

## 🎨 **Features**

### **Form Validation:**
- ✅ All fields required
- ✅ Rating validation (1-5)
- ✅ Input sanitization
- ✅ Error messages

### **UI/UX:**
- ✅ Responsive Bootstrap design
- ✅ Star rating display
- ✅ Flash messages for feedback
- ✅ Clean table layout
- ✅ Mobile-friendly navigation

### **Database Features:**
- ✅ Automatic table creation
- ✅ MySQL and SQLite support
- ✅ Environment-based configuration
- ✅ Error handling and logging

## 🔧 **Configuration**

The application uses `config.py` for centralized configuration:

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE')
```

## 🐛 **Troubleshooting**

### **MySQL Connection Issues:**
1. Ensure MySQL server is running
2. Check credentials in `.env` file
3. Verify MySQL user permissions

### **SQLite Issues:**
1. Check file permissions
2. Ensure write access to project directory

### **Port Issues:**
- Change port in `app.py`: `app.run(debug=True, port=5001)`

## 📝 **Development Notes**

- **Database:** Supports both MySQL and SQLite
- **Templates:** Uses Jinja2 with Bootstrap
- **Validation:** Client and server-side validation
- **Security:** Environment variables for sensitive data
- **Error Handling:** Comprehensive error messages

## 🎯 **Skills Demonstrated**

✅ **Flask Routing & Templating**
✅ **MySQL Database Integration** 
✅ **HTML Form Handling**
✅ **Bootstrap Layout**
✅ **Python Code Structure**
✅ **Environment Configuration**
✅ **Error Handling**
✅ **Form Validation** 