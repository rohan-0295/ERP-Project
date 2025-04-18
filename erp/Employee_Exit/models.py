from django.db import models
from employee.models import Employee

class EmployeeExit(models.Model):
    exit_choices = [
        ('Resignation', 'Resignation'),
        ('Termination', 'Termination'),
        ('Retirement', 'Retirement'),
        ('Other', 'Other'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    exit_type = models.CharField(max_length=20, choices=exit_choices)
    exit_date = models.DateField()
    last_working_day = models.DateField()
    exit_interview_conducted = models.BooleanField(default=False)
    exit_reason = models.TextField(blank=True, null=True)  # Reason for resignation/termination
    assets_returned = models.BooleanField(default=False)
    clearance_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.exit_type} - {self.exit_date}"

    class Meta:
        verbose_name = "Employee Exit"
        verbose_name_plural = "Employee Exits"
