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

## 🧠 Models Overview

### 📂 Category
- category_name → Name of category
- created_at → Creation time
- updated_at → Last update time

---

### 📝 Blog
- title → Blog title
- slug → SEO-friendly URL
- category → ForeignKey (Category)
- author → Django User (ForeignKey)
- featured_image → Blog image
- short_description → Preview text
- blog_body → Full content
- status → Draft / Published
- is_featured → Featured post flag
- views → Blog view counter
- likes → Like counter
- saved_by → Users who bookmarked post (ManyToMany)
- created_at → Created time
- updated_at → Updated time

---

### 💬 Comment
- blog → Related blog (ForeignKey)
- name → Commenter name
- text → Comment content
- created_at → Time of comment

---

### 📩 Contact
- name → User name
- email → Email address
- message → Contact message
- is_read → Admin read status
- created_at → Submission time
## 📌 Future Improvements

-AI -integration



---

## 👨‍💻 Author

Developed by **Ritika Sharma**

---