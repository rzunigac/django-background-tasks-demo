# DEMO: Django Async Scheduler

This project is a simple demo Django application, for educational purposes, that demonstrates how to schedule and manage asynchronous tasks using `django-background-tasks`. The app allows users to trigger an asynchronous task via a web interface, which simulates sending an email and displays scheduled tasks.

## Features

- Asynchronously schedule tasks (e.g., send emails).
- Display a list of scheduled tasks on the success page.
- Use `django-background-tasks` for handling background tasks.

## Requirements

See requirements.txt for versions used.

- Python 3.x
- Django
- `django-background-tasks`

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

## Usage

1. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2. **Start the background task processor:**

    ```bash
    python manage.py process_tasks
    ```

3. **Visit the app in your browser:**

    Go to `http://127.0.0.1:8000/` and trigger an email by clicking the button.

4. **View scheduled tasks:**

    After scheduling a task, you will be redirected to a success page that displays all the scheduled tasks.

**Alternatively, there is a helper script that performs pending migrations, and starts both services the django app and the task processor. It kills the app and the task processor when it exits.**
