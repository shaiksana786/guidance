import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_guidance_config.settings')

try:
    django.setup()
except Exception as e:
    print(f"Error during Django setup: {e}", file=sys.stderr)
    sys.exit(1)

from django.contrib.auth.models import User

try:
    # Create admin user
    User.objects.filter(username='admin').delete()
    admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print(f"✓ Admin user created: {admin.username}")

    # Try to create demo student if models exist
    try:
        from guidance.models import Student, CareerProgress
        User.objects.filter(username='student').delete()
        user = User.objects.create_user(username='student', email='student@example.com', password='demo123')
        student = Student.objects.create(user=user, roll_number='BT19001', branch='CSE', year=1)
        CareerProgress.objects.create(student=student)
        print(f"✓ Demo student created: {user.username} - {student.branch}")
    except Exception as e:
        print(f"⚠ Could not create demo student: {e}")

    print("\n" + "="*40)
    print("LOGIN CREDENTIALS")
    print("="*40)
    print("Admin Panel:")
    print("  Username: admin")
    print("  Password: admin123")
    print("="*40)

except Exception as e:
    print(f"✗ Error creating users: {e}", file=sys.stderr)
    sys.exit(1)
