#!/bin/bash
set -e

cd student-guidance-platform--main/student_guidance

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Creating admin user..."
python setup_users.py || echo "Warning: setup_users.py failed, but continuing..."

echo "Build completed!"