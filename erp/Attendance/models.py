from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee
from datetime import datetime, date


# WorkShifts model to define different shift types
class WorkShifts(models.Model):
    SHIFT_CHOICES = [
        ("Morning", "Morning Shift"),
        ("Night", "Night Shift"),
        ("Evening", "Evening Shift"),
        ("Graveyard", "Graveyard Shift"),
    ]

    name = models.CharField(max_length=100, unique=True)
    shift_type = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"


# Attendance model to track employee attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.ForeignKey(WorkShifts, on_delete=models.SET_NULL, null=True, blank=True)
    clock_in = models.TimeField(null=True, blank=True)
    clock_out = models.TimeField(null=True, blank=True)
    is_present = models.BooleanField(default=True)

    def total_hours_worked(self):
        if self.clock_in and self.clock_out:
            duration = (datetime.combine(date.today(), self.clock_out) - 
                        datetime.combine(date.today(), self.clock_in)).seconds / 3600
            return round(duration, 2)
        return 0

    def __str__(self):
        return f"{self.employee} - {self.date} - {'Present' if self.is_present else 'Absent'}"


# Leave model for applying leaves
class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('SICK', 'Sick Leave'),
        ('VACATION', 'Vacation'),
        ('CASUAL', 'Casual Leave'),
        ('EMERGENCY', 'Emergency Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"


# LeaveApproval model for approving/rejecting leaves
class LeaveApproval(models.Model):
    LEAVE_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=LEAVE_STATUS_CHOICES, default='PENDING')
    decision_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.leave.employee} - {self.status}"
