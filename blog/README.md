# 📝 Django Blog Website

A simple blog website built using Django where users can read and manage blog posts with categories, featured posts, and admin control.

---

## 🚀 Features

- Create, update, and delete blog posts (Admin only)
- Category-wise blog system
- Featured posts section on homepage
- Slug-based SEO friendly URLs
- Image upload support for blogs
- Search and filter in admin panel
- Clean and responsive UI

---

## 🛠️ Tech Stack

- Python
- Django Framework
- SQLite Database
- HTML, CSS (Bootstrap)
- Django Admin Panel

---

## 📁 Project Structure
BlogProject/
│
├── blog/ # Project settings
├── blogapp/ # Main blog app
├── templates/ # HTML files
├── static/ # CSS/JS files
├── media/ # Uploaded images
├── db.sqlite3 # Database
└── manage.py

---


Login with superuser credentials.

---

## 🧠 Models

### Category
- category_name
- slug
- created_at

### Blog
- title
- slug
- category (ForeignKey)
- author
- featured_image
- short_description
- blog_body
- status (Draft/Published)
- is_featured
- created_at

---

## 📌 Future Improvements

-AI -integration



---

## 👨‍💻 Author

Developed by **Ritika Sharma**

---