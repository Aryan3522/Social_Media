# 📸 Social Media Posting Platform (Django)

A Django-based social platform where users can create posts with images or videos, interact through likes, comments, and sharing, and explore content posted by other users.

This project is **open source and beginner-friendly**, making it a great place for developers to start contributing to Django applications and collaborative development.

We welcome **new contributors, first-time open source contributors, and experienced developers** to improve and expand the platform.

---

# 🚀 Features

Current functionality includes:

* User authentication (signup & login)
* Create posts with images or videos
* Like posts
* Comment on posts
* Share posts
* User-based content display
* Django admin panel for content management
* Media file uploads

The goal is to evolve this project into a **full-featured social platform while keeping the architecture easy to understand for contributors.**

---

# 🧰 Tech Stack

Backend

* Python
* Django

Database

* MySQL

Other Tools

* Pillow (image processing)
* Django templates
* HTML / CSS / JavaScript

---

# ⚙️ Running the Project Locally

Follow these steps to run the project on your machine.

---

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 3. Activate the Environment

### Windows

```bash
.\.venv\Scripts\activate
```

### Mac / Linux

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install django pillow mysqlclient django-cors-headers
```

---

## 5. Configure Database

Create a MySQL database:

```sql
CREATE DATABASE auth_app_db;
```

Then update the database settings inside:

```
myStore/settings.py
```

Example configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth_app_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

---

## 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Run the Development Server

Start the Django server with:

```bash
python manage.py runserver
```

Then open your browser and go to:

```
http://127.0.0.1:8000
```

---

# 📂 Project Structure (Simplified)

```
project-root
│
├── myStore
│   ├── settings.py
│   ├── urls.py
│
├── course
│   ├── models.py
│   ├── views.py
│   ├── templates
│   ├── static
│
├── media
├── manage.py
```

---

# 🤝 Contributing

This repository is **open for open source contributions**.

We especially encourage **first-time contributors** to participate.

---

## Contribution Workflow

1. Fork the repository

2. Clone your fork

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

3. Create a new branch

```bash
git checkout -b feature/your-feature-name
```

4. Make your changes

5. Commit your changes

```bash
git commit -m "Add: description of the improvement"
```

6. Push the branch

```bash
git push origin feature/your-feature-name
```

7. Open a Pull Request

---

# 💡 Contribution Ideas

Here are some areas where contributors can help:

* Improve UI / UX
* Add pagination for posts
* Implement follow / unfollow system
* Improve like/comment logic
* Add notifications
* Add API endpoints
* Improve security and validation
* Write tests
* Improve documentation

Issues labeled **`good first issue`** are ideal for beginners.

---

# 🐛 Reporting Bugs

If you find a bug:

1. Open an issue
2. Provide steps to reproduce
3. Include screenshots or error messages if possible

---

# 🌱 Good for Beginners

If you're new to open source:

* Start with small improvements
* Fix minor bugs
* Improve documentation
* Work on issues labeled **good first issue**

Every contribution is valuable.

---

# ⭐ Support the Project

If you find this project useful:

* Star the repository
* Share it with other developers
* Contribute improvements

---

# 🙌 Contributors

Thanks to everyone who contributes and helps improve this project.

Open source grows through collaboration, and every contribution matters.
