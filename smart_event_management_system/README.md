# Smart Event Management System

A beginner-friendly event booking website built with **HTML, CSS, Python, Django, and SQLite**. It includes a responsive homepage, search and category filters, user accounts, event registration, seat tracking, a personal dashboard, and a staff-only overview.

## Features

- Professional four-slide homepage carousel covering discovery, learning, networking, and community events.
- Browse upcoming events and filter them by name, place, or category.
- Create an account, log in, and log out securely using Django authentication.
- View each event's date, venue, description, capacity, and available seats.
- Register for an event while seats are available; duplicate registrations are blocked.
- View and cancel your own registrations from **My bookings**.
- Staff-only control centre with totals and recent activity.
- Django Admin for creating, editing, and deleting events and managing registrations.
- Responsive layout for desktop, tablet, and mobile.

## Run this project in VS Code (Windows)

### 1. Install Python

Install Python 3.11 or newer from https://www.python.org/downloads/ and enable **Add Python to PATH** during setup.

### 2. Open the project

Extract the ZIP, open the `smart_event_management_system` folder in VS Code, and open **Terminal → New Terminal**.

### 3. Create and activate a virtual environment

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 4. Install Django

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Create the database tables

```powershell
python manage.py migrate
```

### 6. Add sample events

```powershell
python manage.py seed_events
```

This command adds six sample events with future dates. It is safe to run more than once; existing sample event titles are not duplicated.

### 7. Create an administrator account

```powershell
python manage.py createsuperuser
```

Follow the prompts to create a username and password. This account can manage event data.

### 8. Start the website

```powershell
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Important pages

- Home page: `http://127.0.0.1:8000/`
- My bookings: `http://127.0.0.1:8000/dashboard/` (login required)
- Staff control centre: `http://127.0.0.1:8000/control-center/` (staff account required)
- Django Admin: `http://127.0.0.1:8000/django-admin/`

To add, edit, or delete events, sign in to Django Admin with the superuser you created, then open **Events → Events**.

## Project structure

```text
smart_event_management_system/
├── manage.py
├── requirements.txt
├── README.md
├── eventhub/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── events/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/seed_events.py
├── templates/
│   ├── base.html
│   ├── events/
│   └── registration/
├── static/css/style.css
    └── js/carousel.js
```

## Homepage carousel

The homepage contains four feature slides. Use the arrow buttons or slide dots to navigate; the carousel advances automatically, pauses while hovered or focused, and respects the browser preference for reduced motion.

## Technologies used

- **Frontend:** HTML5, CSS3, responsive design
- **Backend:** Python and Django
- **Database:** SQLite (created locally as `db.sqlite3`)
- **Authentication:** Django's built-in user authentication and CSRF protection

## Learning / production note

This project is intended for learning and local development. Before putting it on the public internet, set `DEBUG = False`, use a private environment variable for `SECRET_KEY`, configure `ALLOWED_HOSTS`, HTTPS, email, and a production database, and review Django's deployment checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/.
