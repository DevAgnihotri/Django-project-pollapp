# Creating the Polls App in Django

This guide explains how to create a simple polls app in Django. A **Django app** is a self-contained module that performs a specific function, like a blog or a voting system. Multiple apps can be combined into a **Django project**.

### Steps Covered:

1. **Creating the Polls App** – Generating the necessary files and folders.
2. **Writing a View** – Creating a function to return a response.
3. **Defining URL Patterns** – Connecting views to specific web addresses.
4. **Adding the Polls App to the Project** – Making it accessible via the main project.
5. **Running the App** – Checking if everything works properly.
6. **Understanding URL Routing** – Learning how Django processes URLs.
7. **Django Database Setup and Model Creation**

---

## 📌 Setting Up the Polls App

Make sure the terminal is in the same directory as `manage.py`, then run:

```bash
python manage.py startapp polls
```

This command does the following:

- Uses `startapp` to create a new app named `polls`.
- Generates a folder named `polls/` containing important files.

The new app's folder structure:

```
polls/
    __init__.py         # Marks this as a Python package
    admin.py            # Configuration for Django’s admin interface
    apps.py             # App-specific configuration
    migrations/         # Stores database migrations
        __init__.py
    models.py           # Defines database structure for the app
    tests.py            # Used to write tests for the app
    views.py            # Handles what users see in the browser
```

---

## 🌐 Writing the First View

A **view** in Django processes requests and returns responses. To create a basic view:

Open `polls/views.py` and add this line to import `HttpResponse`:

```python
from django.http import HttpResponse
```

Now, define a function that will return a response:

```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Explanation:

- `HttpResponse` is used to send a simple text response.
- `index(request)` is a function that takes an HTTP request and returns `"Hello, world. You're at the polls index."`

This function will display text when someone visits the polls page.

---

## 🔗 Creating URLs for the Polls App

Django needs a way to match URLs to views. To define a URL pattern for the `index` view:

Create a new file `polls/urls.py` and add this import statement:

```python
from django.urls import path
from . import views
```

Now, add the URL pattern inside the `urlpatterns` list:

```python
urlpatterns = [
    path("", views.index, name="index"),
]
```

### Explanation:

- `path("", views.index, name="index")` associates the root URL of `polls/` with the `index` function.
- `name="index"` makes it easier to reference this URL elsewhere in Django.

Now, Django knows to display the `index` view when someone visits `/polls/`.

---

## 🏠 Connecting Polls URLs to the Project

To make the `polls/` URLs accessible, update `mysite/urls.py`:
Add this import statement at the top:

```python
from django.urls import include, path
```

Now, modify the `urlpatterns` list to include the `polls` app:

```python
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

### Explanation:

- `include("polls.urls")` tells Django to look inside `polls/urls.py` for more URL patterns.
- Now, any request to `/polls/` is sent to the `polls` app’s `urls.py`.
- `admin.site.urls` handles Django’s built-in admin panel.

---

## 🚀 Running the Polls App

To see if everything works, start Django’s development server:

```bash
python manage.py runserver
```

Then, visit:

```
http://localhost:8000/polls/
```

If everything is set up correctly, the message `"Hello, world. You're at the polls index."` should appear in the browser.

### Troubleshooting:

- If the page doesn’t load, make sure the server is running (`runserver` command).
- Ensure you typed `http://localhost:8000/polls/` and not `http://localhost:8000/`.

---

## 🛠️ Understanding `path()` Function Arguments

| Argument   | Description                                          |
| ---------- | ---------------------------------------------------- |
| **route**  | URL pattern to match (e.g., `"polls/"`)              |
| **view**   | Function to handle the request (e.g., `views.index`) |
| **kwargs** | Optional extra arguments passed to the view          |
| **name**   | Name of the URL pattern, useful for referencing      |

Django checks each URL in `urlpatterns` from top to bottom and matches the request to a pattern.

# Django Database Setup and Model Creation

Key steps involved in setting up your database and creating models in a Django project.

## 📝 Steps Overview

1. **Database Setup:** Configure your Django project to use SQLite or another database like PostgreSQL.
2. **Creating Models:** Define your data structure using Django's model system.
3. **Activating Models:** Add your app to `INSTALLED_APPS`, make migrations, and apply them.
   - _Specifically_: Add `"polls.apps.PollsConfig"` to register your app.
4. **Using the API:** Use the Django shell to interact with the database, improve model readability, and add utility methods.
5. **Updating Models:** Learn how to safely make changes to your models and reflect those changes in the database.

---

## 🎞 1. Database Setup

### Default Configuration

- Django uses **SQLite** by default.
- Ideal for beginners and testing.
- No additional installation is required.

### Switching Databases

To use PostgreSQL, MySQL, or Oracle:

1. Install appropriate database bindings.
2. Update `mysite/settings.py`:
   - `ENGINE`: e.g., `'django.db.backends.postgresql'`
   - `NAME`: name of your database or full path if using SQLite
   - Add `USER`, `PASSWORD`, and `HOST` (for non-SQLite DBs).

### Time Zone

- Set `TIME_ZONE` in `settings.py` to your local time zone.

### Run Migrations

Create the necessary database tables:

```bash
python manage.py migrate
```

---

## 🧱 2. Creating Models

### Philosophy

- A **model** is the source of truth for your data structure.
- Django uses models to generate database schemas and APIs.

### Example Models in `polls/models.py`

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

**Explanation:**

- `models.Model`: Every model inherits from Django's base `Model` class.
- `CharField`: Used for storing short text (question or choice).
- `DateTimeField`: Stores date and time info.
- `ForeignKey`: Defines a many-to-one relationship. Each choice is linked to a question.
- `on_delete=models.CASCADE`: If a question is deleted, all related choices are also deleted.
- `default=0`: Sets the default vote count to zero.

---

## 📢 3. Activating Models

### Add App to Project

Edit `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    ... # other default apps
]
```

**Why this line is important:**

- It registers your app with the Django project.
- `"polls.apps.PollsConfig"` points to the app configuration class, allowing future customization.
- Enables Django to recognize models, apply migrations, and run app-specific logic.

### Create Migrations

```bash
python manage.py makemigrations polls
```

### View SQL of Migration (Optional)

```bash
python manage.py sqlmigrate polls 0001
```

### Apply Migrations

```bash
python manage.py migrate
```

---

## 🥪 4. Using the API

### Enter Django Shell

```bash
python manage.py shell
```

### Improving Model Readability

Add `__str__` methods:

```python
class Question(models.Model):
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
```

- `__str__`: Returns a human-readable string for each object.
- Helps with readability in the admin panel and shell.

### Add Custom Method

```python
import datetime
from django.utils import timezone

class Question(models.Model):
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

**What's Happening Here:**

- This method checks if a question was published within the last 24 hours.
- `timezone.now()`: Gets the current time (timezone-aware).
- `datetime.timedelta(days=1)`: Subtracts one day from the current time.
- `self.pub_date >= ...`: Compares the question's publication date to check if it's recent.

**Why Use This?**

- Useful in templates, admin panel, or views to filter and show only recent questions.
- Improves user experience by showing only fresh content.

---

## 🛠 5. Summary: Changing Models in Django

1. Modify `models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`

These steps ensure your database and code remain in sync, and changes are version-controlled via migration files.
