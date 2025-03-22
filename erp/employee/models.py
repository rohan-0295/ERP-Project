from django.db import models
from department.models import Department

class Employee(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CON', 'Contractor'),
        ('INT', 'Intern'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('ON_LEAVE', 'On Leave'),
    ]

    employee_id = models.CharField(max_length=20, unique=True, blank=True)
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_hired = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            # Use department's dept_id if available, otherwise use default 'EMP'
            prefix = self.department.dept_id if self.department and self.department.dept_id else 'EMP'
            last_employee = Employee.objects.filter(employee_id__startswith=prefix).order_by('-employee_id').first()
            
            if last_employee and last_employee.employee_id.startswith(prefix):
                last_number = int(''.join(filter(str.isdigit, last_employee.employee_id[len(prefix):])))
                new_number = last_number + 1
            else:
                new_number = 1

            self.employee_id = f"{prefix}{new_number:03d}"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.job_title}"


class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE,null=True,blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
