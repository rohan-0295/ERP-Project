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
    JOB_TITLE_CHOICES = [
        ('SE', 'Software Engineer'),
        ('SSE', 'Senior Software Engineer'),
        ('TL', 'Team Lead'),
        ('PM', 'Project Manager'),
        ('HR', 'HR Manager'),
        ('DA', 'Data Analyst'),
        ('DS', 'Data Scientist'),
        ('DEV', 'Developer'),
    ]

    employee_id = models.CharField(max_length=20, unique=True, blank=True)
    job_title = models.CharField(max_length=50, choices=JOB_TITLE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_hired = models.DateField()

    def save(self, *args, **kwargs):
        if not self.employee_id:
            prefix = 'EMP'
            if self.department and self.department.dept_id:
                prefix = self.department.dept_id
            last_employee = Employee.objects.filter(employee_id__startswith=prefix).order_by('-employee_id').first()
            try:
                if last_employee:
                    last_number = int(''.join(filter(str.isdigit, last_employee.employee_id[len(prefix):])))
                    new_number = last_number + 1
                else:
                    new_number = 1
            except (ValueError, TypeError):
                new_number = 1
            self.employee_id = f"{prefix}{new_number:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.get_job_title_display()}"

    class Meta:
        ordering = ['employee_id']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class EmployeeProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.employee.employee_id if self.employee else 'Unlinked'})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name']
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"


# Optional: Model for a database view (active full-time employees)
class ActiveFulltimeEmployee(models.Model):
    employee_id = models.IntegerField(primary_key=True)  # Tell Django to use this as the unique identifier
    full_name = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    class Meta:
        managed = False  # Not managed by Django; corresponds to a database view
        db_table = 'active_fulltime_employees'
