# Smart Event Management System

A web-based application built with Python and Django to simplify event management, online registration, and seat booking.

## About the Project

The Smart Event Management System helps users explore upcoming events, register for events, and manage their bookings. Administrators can create and manage events, track registrations, and monitor seat availability through the admin dashboard.

The project is designed with a clean, responsive interface that works on desktop and mobile devices.

## Features

- **User Authentication:** User registration and login.
- **Event Management:** Create, update, and delete events.
- **Event Registration:** Register for available events.
- **Seat Availability:** Track available seats and event capacity.
- **User Dashboard:** View registered events and booking details.
- **Admin Dashboard:** Manage events, users, and registrations.
- **Responsive Design:** Supports desktop, tablet, and mobile screens.
- **Database Integration:** Store application data using SQLite for local development.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Website structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive features |
| SQLite | Development database |
| Git and GitHub | Version control |

## Project Structure

```text
smart_event_management_system/
├── manage.py
├── requirements.txt
├── build.sh
├── eventhub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events/
├── templates/
└── static/
```

*Note: The exact folders may vary depending on your project files.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/580shyam/smart-event-management-portal.git
```

### 2. Open the Project Folder

```bash
cd smart-event-management-portal/smart_event_management_system
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Add Sample Events

If the project includes the `seed_events` management command, run:

```bash
python manage.py seed_events
```

### 7. Create an Admin Account

```bash
python manage.py createsuperuser
```

Follow the prompts to set your username and password.

### 8. Start the Development Server

```bash
python manage.py runserver
```

Open the website in your browser:

http://127.0.0.1:8000/

## Admin Panel

To manage events and users, open:

http://127.0.0.1:8000/django-admin/

Log in using your superuser credentials.

## Deployment

The application can be deployed to a suitable Django hosting platform, such as Render. Production deployment requires appropriate security settings, environment variables, static-file configuration, and a suitable database.

GitHub Pages supports static websites only and cannot run the Django backend.

## Future Enhancements

- Email notifications for event registrations.
- Waitlist management for fully booked events.
- Event search and category filters.
- Registration analytics and reports.
- Online payment integration.

## Author

**Shyam Sundar Kumar**

GitHub: https://github.com/580shyam

## License

This project is intended for educational and portfolio purposes. Add a suitable open-source license if you plan to distribute it publicly.
