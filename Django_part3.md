# Setting up Django Admin Setup

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Step 1: Creating a Superuser](#step-1-creating-a-superuser)
3. [Step 2: Starting the Development Server](#step-2-starting-the-development-server)
4. [Step 3: Accessing the Admin Site](#step-3-accessing-the-admin-site)
5. [Step 4: Registering Your App Models](#step-4-registering-your-app-models)
6. [Step 5: Exploring Admin Features](#step-5-exploring-admin-features)
7. [Conclusion](#conclusion)

---

## 🧠 Introduction

The Django Admin site is a built-in interface that allows developers and admins to manage application data without having to create separate UI pages. It's a powerful feature provided by Django that lets you:

- Add, edit, or delete records from the database.
- View and manage users, groups, and permissions.
- Easily manage your custom models through auto-generated forms.

To use the Django Admin, you need to:

1. Create a superuser account.
2. Start the Django development server.
3. Register your models to make them manageable via the admin interface.

---

## ✅ Step 1: Creating a Superuser

Before accessing the admin site, you must create a superuser account. A **superuser** is a Django user with full admin rights.

### 🔧 Command:

```bash
python manage.py createsuperuser
```

### 📥 What this does:

- It starts an interactive prompt where you need to enter:
  - `Username`: e.g., `admin`
  - `Email address`: e.g., `admin@example.com`
  - `Password` (enter twice to confirm)

### ✅ Example Output:

```text
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

Once completed, admin user is ready!

---

## 🚀 Step 2: Starting the Development Server

To access the Django Admin, the project must be running.

### 🔧 Command:

```bash
python manage.py runserver
```

### 🖥️ Access URL:

Open your web browser and visit:

```
http://127.0.0.1:8000/admin/
```

This will open the admin login page.

---

![Alt text](https://docs.djangoproject.com/en/4.2/_images/admin01.png)

## 🔐 Step 3: Accessing the Admin Site

Use the credentials you created in Step 1 to log in.

### 🧾 What you'll see:

- **Login page** – Enter your username and password.
- **Admin dashboard** – After logging in, you'll see an index page listing the available models.
- By default, you’ll see:
  - **Groups**
  - **Users**

These are provided by Django's built-in `django.contrib.auth` framework.

---

## 🧩 Step 4: Registering Your App Models

To manage your own app's models (e.g., from a `polls` app), you need to register them with the admin site.

### 📁 Open this file:

```
polls/admin.py
```

### ✍️ Add the following code:

```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

### 💡 Explanation:

- `admin.site.register(Question)` tells Django to include the `Question` model in the admin interface.
- This will make it visible and editable on the admin dashboard.

---

## 🧭 Step 5: Exploring Admin Features

Once your model is registered, refresh the admin page. You’ll now see the `Question` model listed.

### 📋 On clicking "Questions", you'll see:

- A list of all `Question` objects in the database.
- You can:
  - **Edit existing entries**
  - **Add new ones**
  - **Delete entries**

### ✍️ Editing a Question:

- The form is auto-generated based on the `Question` model.
- Field types like `DateTimeField` and `CharField` render as appropriate input fields.
- You’ll also get useful UI features like:
  - "Today" and "Now" buttons for date/time fields
  - Calendar and clock popups

### 🧰 Save Options:

- **Save** – Saves and goes back to list
- **Save and continue editing** – Saves and stays on the page
- **Save and add another** – Saves and opens a new blank form
- **Delete** – Deletes the record with confirmation

### 🕓 Viewing History:

Click the **"History"** button to see a log of all changes to the object — who changed what, and when.

### ⏰ TimeZone Note:

If “Date published” shows the wrong time, update your project’s `TIME_ZONE` setting in `settings.py`.

---

## ✅ Conclusion

You’ve now:

- Created a Django superuser
- Started the development server
- Logged into the admin panel
- Registered your custom model
- Explored admin features

The Django Admin is incredibly powerful and can help speed up your development and testing process. Once you're comfortable, move on to adding more views and functionalities to your app!

---

👣 Next Step: Continue with the next part of the tutorial to learn how to add custom views and enhance your app’s features.
