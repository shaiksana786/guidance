from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from guidance.models import Student, CareerProgress

class Command(BaseCommand):
    help = 'Create admin and demo users'

    def handle(self, *args, **options):
        # Create admin user
        User.objects.filter(username='admin').delete()
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        self.stdout.write(
            self.style.SUCCESS(f'✓ Admin user created: {admin.username}')
        )

        # Create demo student
        User.objects.filter(username='student').delete()
        user = User.objects.create_user(username='student', email='student@example.com', password='demo123')
        student = Student.objects.create(user=user, roll_number='BT19001', branch='CSE', year=1)
        CareerProgress.objects.create(student=student)
        self.stdout.write(
            self.style.SUCCESS(f'✓ Demo student created: {user.username} - {student.branch}')
        )

        self.stdout.write('\n' + '='*40)
        self.stdout.write('LOGIN CREDENTIALS')
        self.stdout.write('='*40)
        self.stdout.write('Admin Panel:')
        self.stdout.write('  Username: admin')
        self.stdout.write('  Password: admin123')
        self.stdout.write('\nStudent Account:')
        self.stdout.write('  Username: student')
        self.stdout.write('  Password: demo123')
        self.stdout.write('='*40)