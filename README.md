Scheduler App
Overview

Scheduler App is a web-based application that automatically generates feasible schedules based on user-defined constraints. It uses constraint programming to ensure that all assignments are conflict-free and adhere to scheduling rules such as availability and workload limits.

The application is suitable for use cases like employee shift scheduling, study timetables, or basic resource allocation problems.

Features

Web-based user interface

Automatic schedule generation

Constraint-based assignment (no conflicts)

One task per person per time slot

Scalable backend architecture

Production-ready deployment setup

Technology Stack

Backend: Python, Flask

Scheduling Engine: Google OR-Tools (CP-SAT Solver)

Web Server: Gunicorn

Frontend: HTML (Jinja2 templates)

Deployment Platform: Render

Project Structure
scheduler_app/
├── app.py
├── scheduler.py
├── requirements.txt
├── gunicorn.conf.py
└── templates/
    ├── index.html
    └── result.html

How It Works

The user enters:

A list of people

A list of tasks

A list of time slots

The system models the problem as a constraint satisfaction problem.

Google OR-Tools computes a valid schedule if one exists.

The generated schedule is displayed in the browser.

Local Setup Instructions
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/scheduler-app.git
cd scheduler-app

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000

Deployment

The application is ready for cloud deployment using Render.

Deployment settings:

Runtime: Python 3.10

Build Command:

pip install -r requirements.txt


Start Command:

gunicorn app:app

Example Input

People: Alice, Bob

Tasks: Support, Development

Time Slots: Morning, Afternoon

Future Enhancements

Availability selection per person

Preference-based optimization

Weekly and monthly scheduling

Database integration

User authentication

CSV import/export

License

This project is open-source and available for educational and personal use.
