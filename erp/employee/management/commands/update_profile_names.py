from django.core.management.base import BaseCommand
from employee.models import Employee, EmployeeProfile

class Command(BaseCommand):
    help = 'Check and print EmployeeProfile names linked to each Employee'

    def handle(self, *args, **kwargs):
        employees = Employee.objects.all()
        if not employees.exists():
            self.stdout.write("⚠️ No employees found in the database.")
            return

        for emp in employees:
            profile = EmployeeProfile.objects.filter(employee=emp).first()
            if profile:
                self.stdout.write(f"✅ Profile found for {emp.employee_id}: {profile.full_name}")
            else:
                self.stdout.write(f"❌ Profile not found for Employee ID {emp.employee_id}")
