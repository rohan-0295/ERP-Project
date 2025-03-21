from django.db import models
from employee.models import Employee

class Payroll(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Link to Employee table
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee.employee_id} - {self.salary}"


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
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_date = models.DateField()

    def __str__(self):
        return f"{self.employee.employee_id} - {self.tax_type} - {self.amount}"
