# 📝 Django Blog Website

## 📌 Description
This is a Django-based blog project where users can create, read, update, and delete blog posts. It uses Django MVC architecture with templates, static files, and media support.

---

## 🚀 Features
- CRUD blog posts
- Admin panel
- Media upload support
- Template-based frontend
- Django backend

---

## 🛠️ Tech Stack
- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
## 📁 Project Structure
BlogProject/
│
├── blog/ # Project configuration (settings, urls)
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── blogapp/ # Main application
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ ├── migrations/
│
├── templates/ # HTML templates
│
├── static/ # CSS, JS, images
│
├── media/ # Uploaded media files
│
├── db.sqlite3 # Database (ignored in Git)
│
├── manage.py # Django entry point