from django.db import models
from employee.models import Employee

class Review(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"{self.employee.employee_id} - {self.score}"


class Goal(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('ACHIEVED', 'Achieved')])

    def __str__(self):
        return f"{self.employee.employee_id} - {self.description}"
