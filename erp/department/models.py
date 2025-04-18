from django.db import models

class Department(models.Model):
    # Custom mappings: adjust as needed
    PREFIX_MAP = {
        'Human Resources': 'HR',
        'Information Technology': 'IT',
        'Finance': 'FIN',
        'Marketing': 'MKT',
        'Sales': 'SAL',
        'Production': 'PROD',
        'Logistics': 'LOG',
        'Customer Support': 'SUP',
        'Legal': 'LEG',
        'Research and Development': 'RND',
        'Administration': 'ADM',
        'Public Relations': 'PR',
        'Procurement': 'PRC',
        'Quality Assurance': 'QA',
        'Business Development': 'BD',
        'Engineering': 'ENG',
        'Security': 'SEC',
        'Training': 'TRN',
        'Operations': 'OPS',
        'Facilities': 'FAC',
        'Analytics': 'ANL',
        'Design': 'DSN',
        'Compliance': 'CMP',
        'Strategy': 'STR',
        'Product Management': 'PDM'
        # You can add more if needed
    }

    dept_id = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=75)

    def save(self, *args, **kwargs):
        if not self.dept_id:
            # Get mapped prefix or fallback to first 3 letters
            prefix = self.PREFIX_MAP.get(self.name, self.name[:3].upper())
            last_dept = Department.objects.filter(dept_id__startswith=prefix).order_by('-dept_id').first()

            if last_dept:
                # Extract number part after prefix
                last_number = int(''.join(filter(str.isdigit, last_dept.dept_id[len(prefix):])))
                new_number = last_number + 1
            else:
                new_number = 1

            self.dept_id = f"{prefix}{new_number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
