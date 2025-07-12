# 🎓 School Reviews Flask Application

A modern Flask web application that allows users to submit and view school reviews with support for both MySQL and SQLite databases.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [API Routes](#api-routes)
- [Screenshots](#screenshots)
- [Demo](#demo)
- [Contributing](#contributing)

## 🎯 Overview

This Flask application provides a complete school review system where users can:
- Submit reviews for schools with ratings and comments
- View all submitted reviews in a clean, responsive interface
- Rate schools on a 1-5 scale with detailed feedback
- Experience a modern UI built with Bootstrap

## ✨ Features

- **📝 Review Submission**: Easy-to-use form for adding school reviews
- **⭐ Rating System**: 1-5 star rating with validation
- **📊 Review Display**: Clean table layout showing all reviews
- **🔒 Form Validation**: Client and server-side validation
- **📱 Responsive Design**: Mobile-friendly Bootstrap interface
- **🗄️ Database Flexibility**: Support for both MySQL and SQLite
- **⚙️ Environment Configuration**: Secure credential management

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL / SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Templates**: Jinja2
- **Configuration**: python-dotenv
- **Database Connector**: mysql-connector-python

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- MySQL (optional - SQLite is default)
- pip

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/school_reviews_app.git
cd school_reviews_app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# Copy the example file
cp env_example.txt .env
```

### 4. Configure Database
Choose your database type and configure accordingly:

#### Option A: SQLite (Default)
```bash
DATABASE_TYPE=sqlite
```

#### Option B: MySQL
```bash
DATABASE_TYPE=mysql
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=school_reviews
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Application
Open your browser and navigate to: `http://127.0.0.1:5000`

## 🔧 Environment Variables

Create a `.env` file in the root directory with the following variables:

```bash
# Required
SECRET_KEY=your_secret_key_here
DATABASE_TYPE=sqlite  # or 'mysql'

# MySQL Configuration (only if using MySQL)
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=school_reviews

# SQLite Configuration (only if using SQLite)
SQLITE_DATABASE=school_reviews.db
```

## 🗄️ Database Setup

### MySQL Setup
1. Install MySQL Server
2. Create a database:
```sql
CREATE DATABASE school_reviews;
```
3. Import the schema:
```bash
mysql -u root -p school_reviews < school_reviews.sql
```

### SQLite Setup
The database will be created automatically when you first run the application.

### Database Schema
```sql
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📡 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Redirects to reviews page |
| `/addreview` | GET | Display review submission form |
| `/addreview` | POST | Handle review submission |
| `/reviews` | GET | Display all reviews |

## 📸 Screenshots

### Main Reviews Page
![Reviews Page](screenshots/reviews-page.png)

### Add Review Form
![Add Review Form](screenshots/add-review-form.png)

### Mobile Responsive Design
![Mobile View](screenshots/mobile-view.png)

## 🎥 Demo

### Live Demo
🔗 **Live Demo**: [https://your-demo-link.com](https://your-demo-link.com)

### Demo Video
📹 **Demo Video**: [Google Drive Link](https://drive.google.com/your-video-link) or [YouTube Link](https://youtube.com/your-video-link)

## 📁 Project Structure

```
school_reviews_app/
├── app.py                 # Main Flask application
├── config.py              # Database configuration
├── requirements.txt       # Python dependencies
├── school_reviews.sql    # Database schema and sample data
├── README.md             # This file
├── .env                  # Environment variables (create this)
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── add_review.html   # Add review form
│   └── reviews.html      # Display all reviews
└── static/               # Static files
    └── style.css         # Custom CSS styles
```

## 🐛 Troubleshooting

### Common Issues

**MySQL Connection Error:**
```bash
# Check if MySQL is running
sudo service mysql status

# Verify credentials in .env file
# Ensure database exists
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS school_reviews;"
```

**Port Already in Use:**
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

**Import Errors:**
```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yashh-17](https://github.com/yashh-17)
- LinkedIn: [Yaswanth Vuyyuru](https://www.linkedin.com/in/yaswanth-vuyyuru-634a84287/)

---

⭐ **Star this repository if you found it helpful!** 
