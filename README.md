The Patient Scheduler is a Django-based appointment management system that allows patients to book, reschedule, and cancel appointments with available healthcare providers. It provides an intuitive, secure interface for users to manage appointments efficiently.

# Features

- User Authentication

- Secure login/logout functionality using Django’s authentication system.

- Separate access for patients and providers.

- Appointment Management

- Book available time slots with specific providers.

- Prevents overlapping appointments.

- Allows patients to reschedule or cancel their bookings.

- Displays upcoming and past appointments in a clean, simple dashboard.

- Provider Management

- Admins can add healthcare providers and define their availability schedules via the Django admin panel.

- Each provider can have multiple availability windows.

- Responsive UI

- Organized interface with consistent navigation and visual feedback.

- Custom CSS for a modern, professional look.

| Category        | Tools / Frameworks        |
| --------------- | ------------------------- |
| Backend         | Django 5.2.7 (Python)     |
| Frontend        | HTML5, CSS3               |
| Database        | SQLite (default)          |
| IDE             | Visual Studio Code        |
| Version Control | Git & GitHub              |
| Deployment      | Localhost / AWS EC2-ready |


# Installation and Setup

 1. Clone the repository
    
    git clone https://github.com/yourusername/patient-scheduler.git
    cd patient-scheduler

 2. Create a virtual environment
    
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate   # macOS/Linux

 3. Install dependencies
    
    pip install Django asgiref sqlparse tzdata

 4. Run migrations
    
    python manage.py makemigrations
    python manage.py migrate

 5. Create a superuser
     
    python manage.py createsuperuser

 6. Run the development server
     
    python manage.py runserver


# How It Works

1. Admin Login:
Admins create providers and define their available time slots in Django Admin.

2. Patient Login:
Patients log in, navigate to the Dashboard, and book an appointment.

3. Validation:
The system prevents overlapping times and ensures providers are available.

4. Management:
Patients can reschedule or cancel existing appointments directly from their dashboard.

# Folder Structure

```
PATIENT-SCHEDULER/
│
├── booking/                     # Core Django app
│   ├── migrations/              # Database migration files
│   ├── templates/booking/       # HTML templates
│   ├── static/booking/          # (optional) app-level static files
│   ├── admin.py                 # Admin registration
│   ├── apps.py
│   ├── forms.py                 # Appointment forms
│   ├── models.py                # Provider, Availability, Appointment
│   ├── urls.py                  # App-specific URL routing
│   ├── views.py                 # Booking, cancel, reschedule views
│
├── scheduler/                   # Project configuration
│   ├── __init__.py
│   ├── settings.py              # Main Django settings
│   ├── urls.py                  # Root URL mapping
│   ├── wsgi.py
│
├── static/css/                  # Global static folder for styles
│   └── style.css
│
├── templates/registration/      # Login and logout templates
│   └── login.html
│
├── db.sqlite3                   # Local database
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

# Contributors

Sid Mehta – Developer
Southern Illinois University, IT & Cybersecurity
   




