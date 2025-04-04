# Learn Django: Make a Simple Website (Easy Guide for Beginners)

This guide explains how to start a website using **Django**, a tool that helps build websites with **Python**. It is written in simple words for beginners around grade 6 level.

This guide covers:
1. [Starting a new Django project 📁](#step-1-start-a-django-project)
2. [Running a test website on a computer 🌐](#step-2-run-the-website)
3. [Understanding important files 🧾](#step-1-start-a-django-project)
4. [Trying small changes and testing them 🧪](#step-3-server-and-port-options)

The example is a basic poll site that lets people vote on simple questions like *"What's your favorite fruit?"* 🍎🍌🍇

---

## 📌 What is Django?
**Django** is a web framework. It is a set of tools for building websites quickly using **Python**, a popular programming language. It includes many ready-to-use parts, so building a website is easier.

---

## ✅ Before Starting
Requirements:
- **Python 3.8 or newer** installed.
- **Django** installed. To install Django:
  ```bash
  pip install Django
  ```
- To check Django is installed:
  ```bash
  python -m django --version
  ```
  A version number (like 4.2) should appear.

---

## 🚀 Step 1: Start a Django Project
### [Go to Step 1](#step-1-start-a-django-project)

In the terminal, run:
```bash
django-admin startproject mysite
```

This command:
- Uses `django-admin`, a tool for Django projects.
- Runs `startproject` to create a new website.
- Makes a folder called `mysite` (this name can be different).

It creates these files:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### File Descriptions:
- `manage.py`: Runs commands for the site.
- `settings.py`: Stores project settings.
- `urls.py`: Tells Django what to show on different pages.

---

## 🌐 Step 2: Run the Website
### [Go to Step 2](#step-2-run-the-website)

Go into the project folder:
```bash
cd mysite
```

Start the server:
```bash
python manage.py runserver
```

- This starts a **development server** for testing.
- Open a browser and go to:
  ```
  http://127.0.0.1:8000/
  ```
- A welcome page should appear. That means Django is working.

---

## ⚙️ Step 3: Server and Port Options
### [Go to Step 3](#step-3-server-and-port-options)

To change the port (default is 8000):
```bash
python manage.py runserver 8080
```
Visit:
```
http://127.0.0.1:8080/
```

To let other devices on the same Wi-Fi see the site:
```bash
python manage.py runserver 0:8000
```

---

## ✅ What’s Next?
After this basic setup:
- [Add an app (a section of the site, like a poll or blog).](#step-1-start-a-django-project)
- [Add a database to save information.](#step-3-server-and-port-options)
- [Create simple pages.](#step-1-start-a-django-project)
- [Use Django admin to manage content.](#step-1-start-a-django-project)

---

## 🧠 Quick Terms to Remember
| Term | What It Means |
|------|----------------|
| **Django** | Tool to make websites using Python |
| **Project** | Full setup of the website |
| **App** | Small part of the website (like a blog or poll) |
| **Terminal** | Place to type computer commands |
| **Server** | Program that runs the website |
| **manage.py** | File used to control the website from the terminal |
