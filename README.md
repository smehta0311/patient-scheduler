🩺 Patient Appointment Scheduler

A full-stack Django web application for managing patient appointments with healthcare providers. Patients can book, reschedule, or cancel appointments, while providers can view and manage their scheduled visits. The system includes modern UI styling, strong validation, and clear user workflows.

📌 Overview

- The Patient Appointment Scheduler helps streamline booking workflows by providing:

- A clean and user-friendly interface

- Full patient and provider functionality

- Time validation and conflict detection

- Professional-grade UI components with polished styling

🚀 Features

👤 Patient Features

- Create an account and log in

- Book appointments with a selected provider

- Select date & time using Flatpickr

- Add a reason for the appointment

- View all appointments in a clean table layout

- Reschedule or cancel active bookings

System prevents:

- Double-booking with the same provider

- Booking in the past

- End time earlier than start time

- Overlapping appointments

🩺 Provider Features

- Log in to access the Provider Dashboard

- View all assigned patient appointments

- See appointment reasons

- Reschedule or cancel appointments

- Canceled/expired appointments appear visually dimmed

🎨 UI / UX Highlights

- Modern pill-shaped navigation buttons

- Distinct color-coded buttons (blue, light-blue, purple)

- Centered dashboard card layout

Styled tables with:

- Zebra striping

- Status badges (BOOKED, RESCHEDULED, CANCELED)

- Action links

- Helpful empty states and clearer messages across the app

🔐 Validation & System Logic

The system includes strong booking validation:

- Disallows booking past dates

- Ensures end time > start time

- Blocks appointments overlapping with existing provider slots

- Prevents double-booking during reschedule

- Provides clear success and error messages

🛠️ Tech Stack
Backend

- Python 3.x

- Django Framework

- SQLite (for development)

- Frontend

- HTML, CSS (custom stylesheet)

- Flatpickr (datetime picker)

Tools

- Visual Studio Code

- Git & GitHub

📂 Project Structure
```
patient-scheduler/
│
├── booking/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/booking/
│   └── static/css/style.css
│
├── scheduler/
│   ├── settings.py
│   └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

🧪 Running the Project Locally

1. Clone the repository:
git clone https://github.com/smehta0311/patient-scheduler.git
cd patient-scheduler

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
 pip install -r requirements.txt

4. Apply migrations:
 python manage.py migrate

5. Run the development server:
python manage.py runserver

6. Open the app:
http://127.0.0.1:8000/

👤 User Role Summary

Patient: Books, views, reschedules, and cancels their own appointments.

Provider: Views all appointments booked with them. Can reschedule or cancel patient appointments.

📜 License

This project is for academic and educational use as part of a senior capstone project.

🙌 Acknowledgements

Developed as part of a senior project showcasing full-stack development, system design, user experience principles, and real-world validation logic using Django.





Git & GitHub
