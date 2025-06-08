# Django Polls Application

A simple web application built with Django that allows users to create and vote on polls. This project demonstrates fundamental Django concepts including models, views, URLs, templates, and database operations.

## 🍴 Fork & Run on Your PC

### Prerequisites

- **Python 3.8+** installed on your system
- **Git** (for cloning/forking)
- **pip** (Python package installer)

### Step 1: Fork/Clone the Project

```bash
# Option 1: Clone directly
git clone <repository-url>
cd "Django pro 1"

# Option 2: Fork on GitHub first, then clone your fork
git clone <your-forked-repository-url>
cd "Django pro 1"
```

### Step 2: Set Up Python Environment (Recommended)

```bash
# Create virtual environment
python -m venv django_env

# Activate virtual environment
# Windows:
django_env\Scripts\activate
# macOS/Linux:
source django_env/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install Django
pip install django

# Verify installation
python -m django --version
```

### Step 4: Set Up Database

```bash
# Apply initial migrations
python manage.py migrate

# Create superuser (optional - for admin access)
python manage.py createsuperuser
```

### Step 5: Run the Development Server

```bash
# Start the server
python manage.py runserver

# Access the application:
# - Main site: http://localhost:8000/
# - Polls app: http://localhost:8000/polls/
# - Admin: http://localhost:8000/admin/
```

### 🚨 Troubleshooting Setup

- **Python not found**: Add Python to your system PATH
- **Django not found**: Run `pip install django` in the correct environment
- **Permission errors**: Use virtual environment or run with appropriate permissions
- **Port 8000 busy**: Use `python manage.py runserver 8080` for different port

---

## 📖 Project Overview

This Django project consists of a polls application where users can:

- View available polls/questions
- Vote on poll choices
- See poll results
- Admin interface for managing polls

## 🏗️ Project Structure

```
Django pro 1/
├── manage.py                 # Django management script
├── mysite/                   # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── polls/                    # Polls application
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── tests.py             # Test cases
│   └── migrations/          # Database migrations
├── Django_part2.md          # Detailed tutorial documentation
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation & Setup

1. **Clone/Navigate to the project directory:**

   ```bash
   cd "d:\PROJECTS\Coursera\Django\Django pro 1"
   ```

2. **Install Django:**

   ```bash
   pip install django
   ```

3. **Verify Django installation:**
   ```bash
   python -m django --version
   ```

### 🏃‍♂️ Running the Project

1. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

3. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

4. **Access the application:**
   - Main site: http://localhost:8000/
   - Polls app: http://localhost:8000/polls/
   - Admin interface: http://localhost:8000/admin/

### 🛠️ Development Workflow

#### Creating the Polls App

```bash
python manage.py startapp polls
```

#### Working with Models

1. **Create/modify models in `polls/models.py`**
2. **Generate migrations:**
   ```bash
   python manage.py makemigrations polls
   ```
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

#### Django Shell for Testing

```bash
python manage.py shell
```

## 📊 Database Models

### Question Model

- `question_text`: CharField (max 200 characters)
- `pub_date`: DateTimeField (publication date)
- `was_published_recently()`: Custom method to check recent publications

### Choice Model

- `question`: ForeignKey to Question
- `choice_text`: CharField (max 200 characters)
- `votes`: IntegerField (default 0)

## 🌐 URL Structure

- `/` - Main site homepage
- `/polls/` - Polls index page
- `/admin/` - Django admin interface

## 📚 Key Django Concepts Covered

1. **Apps and Projects**: Understanding Django's modular structure
2. **Models**: Defining data structure and database schema
3. **Views**: Handling HTTP requests and responses
4. **URLs**: Routing and URL patterns
5. **Migrations**: Database schema management
6. **Admin Interface**: Built-in administrative interface
7. **Django Shell**: Interactive Python environment

## 🔧 Common Commands

| Command                            | Description              |
| ---------------------------------- | ------------------------ |
| `python manage.py runserver`       | Start development server |
| `python manage.py makemigrations`  | Create new migrations    |
| `python manage.py migrate`         | Apply migrations         |
| `python manage.py shell`           | Open Django shell        |
| `python manage.py createsuperuser` | Create admin user        |
| `python manage.py startapp <name>` | Create new app           |

## 📖 Documentation

For detailed step-by-step instructions and explanations, refer to:

- [Django_part2.md](Django_part2.md) - Comprehensive tutorial with code examples

## 🐛 Troubleshooting

### Common Issues

1. **"No module named django" error:**

   ```bash
   pip install django
   ```

2. **"can't open file 'manage.py'" error:**

   - Ensure you're in the correct directory containing `manage.py`

3. **Migration errors:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Server not accessible:**

   - Check if server is running: `python manage.py runserver`
   - Verify URL: http://localhost:8000/polls/

5. **PATH issues on Windows:**

   - Add Python to system PATH during installation
   - Or use `python.exe` instead of `python`

6. **Virtual environment activation issues:**
   ```bash
   # Windows
   django_env\Scripts\activate.bat
   # PowerShell
   django_env\Scripts\Activate.ps1
   ```

## 🎯 Next Steps

1. Add templates for better UI
2. Implement voting functionality
3. Add results display
4. Style with CSS
5. Deploy to production

## 📝 Learning Resources

- [Official Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- Project documentation: [Django_part2.md](Django_part2.md)

---

**Happy coding!** 🚀
