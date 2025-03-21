from django.db import models
from employee.models import Employee

class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('AVAILABLE', 'Available'), ('ASSIGNED', 'Assigned'), ('MAINTENANCE', 'Maintenance')])

    def __str__(self):
        return self.asset_name


class Assignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset.asset_name} - {self.employee.employee_id}"
