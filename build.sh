#!/bin/bash
cd student-guidance-platform--main/student_guidance
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate