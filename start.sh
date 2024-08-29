#!/bin/bash

# Apply database migrations
python manage.py migrate

# Start the Django development server in the background
python manage.py runserver &
RUNSERVER_PID=$!

# Start the background task processor in the background
python manage.py process_tasks &
PROCESS_TASKS_PID=$!

cleanup() {
    echo "Stopping Django server and background task processor..."
    kill $RUNSERVER_PID
    kill $PROCESS_TASKS_PID
    exit 0
}

trap cleanup SIGINT SIGTERM
wait $RUNSERVER_PID
wait $PROCESS_TASKS_PID
