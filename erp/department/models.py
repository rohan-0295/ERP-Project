from django.db import models

class Department(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
        ('SALES', 'Sales'),
        ('PROD', 'Production'),
    ]
    
    PREFIX_MAP = {
        'HR': 'HR',
        'IT': 'IT',
        'FIN': 'FIN',
        'MKT': 'MKT',
        'SALES': 'SALES',
        'PROD': 'PROD',
    }

    dept_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    location = models.CharField(max_length=75)

    def save(self, *args, **kwargs):
        if not self.dept_id:
            prefix = self.PREFIX_MAP.get(self.name, 'DEP')
            last_dept = Department.objects.filter(name=self.name).order_by('-dept_id').first()
            if last_dept and last_dept.dept_id.startswith(prefix):
                # Extract numeric part correctly
                last_number = int(''.join(filter(str.isdigit, last_dept.dept_id[len(prefix):])))
                new_number = last_number + 1
            else:
                new_number = 1

            # Format as HR001, IT002, etc.
            self.dept_id = f"{prefix}{new_number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.dept_id})"


