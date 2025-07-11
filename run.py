#!/usr/bin/env python3
"""
Simple startup script for the School Reviews Flask Application
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("=== School Reviews Flask Application ===")
    print("Starting the application...")
    
    try:
        from app import app, create_database
        
        # Initialize database
        create_database()
        
        # Run the application
        print("✓ Application starting on http://127.0.0.1:5000")
        print("✓ Press Ctrl+C to stop the application")
        app.run(debug=True, host='127.0.0.1', port=5000)
        
    except ImportError as e:
        print(f"✗ Error importing modules: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"✗ Error starting application: {e}") 