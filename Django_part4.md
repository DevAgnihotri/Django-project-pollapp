# 🧱 Writing Views

### ✅ Steps Completed here:

- Added new view functions: `detail()`, `results()`, and `vote()` in `views.py`
- Mapped new views in `polls/urls.py` using `path()`
- Implemented a dynamic index view to fetch and display latest questions
- Created HTML templates for rendering views
- Used Django’s template system for separation of logic and design
- Replaced hard-coded HTML with templates
- Introduced and explained `render()` as a shortcut and its importance
- Used `get_object_or_404()` instead of try/except for better error handling

##### Using the Template System

- Used Django’s **template system** to render dynamic content
- Created a `detail.html` template to display question and its choices
- Replaced hardcoded URLs in templates with `{% url %}` tag
- Introduced the concept of **namespacing URL names**

---

## 🔹 What is a View?

In Django, a **view** is a Python function (or method) that takes a **web request** and returns a **web response**. Views are responsible for processing logic and returning content like HTML pages, JSON, or any other format.

### Example Views in a Blog App:

- Homepage – displays latest blog entries
- Detail page – shows a single blog post
- Archives – filter entries by year/month/day
- Comment action – handles comment posting

### Views in Our Polls App:

- `index` – shows recent questions
- `detail` – displays question and voting form
- `results` – shows voting results
- `vote` – processes vote submissions

## 🔸 URLconf & URL Patterns

Django maps **URLs to views** using **URLconf** (URL configuration).

> Example of a URL pattern: `/newsarchive/<year>/<month>/`

---

## 🥉 Writing More Views in `polls/views.py`

```python
from django.http import HttpResponse

# View: Question detail
# Shows text of the question
# URL: /polls/5/
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# View: Question results
# Shows results for the question
# URL: /polls/5/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# View: Voting action
# Handles the vote
# URL: /polls/5/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

---

## 🛠️ Wire Views into URLs – `polls/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Home page
    path("<int:question_id>/", views.detail, name="detail"),  # Detail page
    path("<int:question_id>/results/", views.results, name="results"),  # Results
    path("<int:question_id>/vote/", views.vote, name="vote"),  # Vote
]
```

📍 Visit URLs like `/polls/34/`, `/polls/34/results/`, and `/polls/34/vote/` in your browser to test!

---

## 🤠 How URL Matching Works:

When `/polls/34/` is requested:

- Django uses `ROOT_URLCONF` → `mysite.urls`
- Matches pattern `'polls/'` → sends remaining `'34/'` to `polls.urls`
- Matches `<int:question_id>/` → Calls:

```python
detail(request=<HttpRequest>, question_id=34)
```

---

## ⚙️ Writing Views That Actually Work

Your view needs to return an **HttpResponse** or raise an **Http404**.

✅ It can read from DB, render a template, generate files, or just return plain text.

### Update `index` to Fetch Latest Questions

```python
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # Fetch top 5 questions
    output = ", ".join([q.question_text for q in latest_question_list])  # Combine texts
    return HttpResponse(output)
```

---

## 📜 Create Templates for Views

Instead of hardcoding HTML, let’s use templates.

📁 Create folder: `polls/templates/polls/`
📄 Inside it, create `index.html`

### 🤠 Why Namespacing?

If multiple apps have `index.html`, Django won't know which one to load. So we use `polls/index.html` path.

### index.html Example:

```html
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}
```

---

## 🎨 Load Template in View – `views.py`

```python
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")  # Load template
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))  # Render and return
```

---

## 🏃‍♂️ Shortcut: `render()`

```python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

### 📀 What is `render()` and Why Use It?

- `render()` is a **shortcut** provided by Django.
- It combines loading a template, filling it with context data, and returning an `HttpResponse` **in one step**.
- It simplifies your view logic and reduces boilerplate code.
- It improves readability and keeps views clean.

### Without `render()`:

```python
from django.template import loader
from django.http import HttpResponse

template = loader.get_template("template.html")
return HttpResponse(template.render(context, request))
```

### With `render()`:

```python
return render(request, "template.html", context)
```

✅ `render()` = load + fill + return

📉 No more need for `loader` and `HttpResponse` for such views.

---

## 🚫 Raising a 404 Error

Update `detail()` to show a proper error if question doesn’t exist.

```python
from django.http import Http404
from django.shortcuts import render
from .models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)  # Get object
    except Question.DoesNotExist:
        raise Http404("Question does not exist")  # Raise 404
    return render(request, "polls/detail.html", {"question": question})
```

📁 Create `polls/templates/polls/detail.html`
📄 Temporary content:

```django
{{ question }}
```

---

## ✨ Shortcut: `get_object_or_404()`

```python
from django.shortcuts import get_object_or_404, render
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # One-liner 404 check, pk is the primary key here
    return render(request, "polls/detail.html", {"question": question})
```

### 📌 Why This Is Better:

- Prevents duplication of try/except blocks
- Keeps views concise
- Maintains loose coupling between model and view

---

## ✅ Summary

In this part, we:

- Defined multiple views in `views.py`
- Mapped those views to URLs
- Pulled data from the database
- Used templates to render dynamic content
- Handled 404 errors properly
- Simplified our views using `render()` and `get_object_or_404()`
- Learned what `render()` does and why it's essential for clean, efficient views

# Using the Template System

### ✅ Steps Completed:

- Used Django’s **template system** to render dynamic content
- Created a `detail.html` template to display question and its choices
- Replaced hardcoded URLs in templates with `{% url %}` tag
- Introduced the concept of **namespacing URL names**

---

## 🧾 Use the Template System

Let’s go back to the `detail()` view in our polls app. Given the context variable `question`, the `polls/detail.html` template might look like:

📄 **polls/templates/polls/detail.html**

```html
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

### 🧠 How It Works:

- `{{ question.question_text }}` uses **dot-lookup syntax**:

  - Django first tries a dictionary lookup → fails
  - Then it tries attribute lookup → succeeds ✅
  - If that fails too, it tries list-index lookup

- In `{% for %}` loop, `question.choice_set.all` is interpreted as a method call → returns an iterable of `Choice` objects

🔗 Refer to the official template guide for more.

---

## 🔗 Removing Hardcoded URLs

Originally, we had this in `polls/index.html`:

```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

📛 **Issue**: This is hardcoded. If URL changes, templates break. Not scalable.

✅ Better Approach: Use `{% url %}` template tag

```html
<li>
  <a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>
</li>
```

🔍 Django uses the `name` argument from `path()` in `polls/urls.py`:

```python
path("<int:question_id>/", views.detail, name="detail")
```

### 🛠️ Changing the Path

To switch to a new path format like `polls/specifics/12/`, just change `urls.py`:

```python
path("specifics/<int:question_id>/", views.detail, name="detail")
```

No template change needed! 🧠

---

## 🧩 Namespacing URL Names

In real-world projects with many apps, multiple apps may have views with the same name (e.g., `detail`). How does Django differentiate them?

🧪 **Solution**: Add **namespace** using `app_name` in `polls/urls.py`:

```python
from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

### ✅ Updated Template:

Change this:

```html
<li>
  <a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>
</li>
```

To this:

```html
<li>
  <a href="{% url 'polls:detail' question.id %}"
    >{{ question.question_text }}</a
  >
</li>
```

This way Django knows you're referring to the `polls` app.

---

## ✅ Summary

- Created and used Django templates to dynamically render question details and choices
- Avoided hardcoded URLs using `{% url %}`
- Made URL patterns robust with **namespacing**

➡️ Up next: Learn how to handle forms and use Django’s generic views in Part 4!
