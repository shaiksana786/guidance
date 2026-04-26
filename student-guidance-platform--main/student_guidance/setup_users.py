import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_guidance_config.settings')
django.setup()

from django.contrib.auth.models import User
from guidance.models import Student, CareerProgress

# Create admin user
User.objects.filter(username='admin').delete()
admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print(f"✓ Admin user created: {admin.username}")

# Create demo student
User.objects.filter(username='student').delete()
user = User.objects.create_user(username='student', email='student@example.com', password='demo123')
student = Student.objects.create(user=user, roll_number='BT19001', branch='CSE', year=1)
CareerProgress.objects.create(student=student)
print(f"✓ Demo student created: {user.username} - {student.branch}")

print("\n" + "="*40)
print("LOGIN CREDENTIALS")
print("="*40)
print("Admin Panel:")
print("  Username: admin")
print("  Password: admin123")
print("\nStudent Account:")
print("  Username: student")
print("  Password: demo123")
print("="*40)
