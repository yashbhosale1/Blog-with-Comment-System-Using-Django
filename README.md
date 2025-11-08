# Django Blog with Comment System

## Features
- User registration, login, logout
- Create, edit, delete posts
- Comment and reply system
- REST API endpoints for posts and comments
- Bootstrap-based UI and pagination

## Quick start
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
5. Run the server:
   ```
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/

## Notes
- This project uses SQLite by default.
- The SECRET_KEY in settings.py is a placeholder. Replace it for production.
