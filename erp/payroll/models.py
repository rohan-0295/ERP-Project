# payroll/models.py

from django.db import models
from employee.models import Employee

class Payroll(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Link to Employee table
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Gross salary
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Net salary (calculated by trigger)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.gross_salary}"

class Bonus(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Link to Employee table
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_date = models.DateField()
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.amount}"

class Tax(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Link to Employee table
    tax_type = models.CharField(max_length=50)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Tax percentage (e.g., 12 for 12%)
    tax_date = models.DateField()

    def __str__(self):
        return f"{self.employee.employee_id} - {self.tax_type} - {self.tax_percentage}%"
