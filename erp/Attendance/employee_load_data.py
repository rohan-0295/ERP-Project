import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp.settings")
django.setup()

from employee.models import Employee

# Step 1: Delete all existing employee data
Employee.objects.all().delete()
print("✅ All existing employee records have been deleted.")

# Step 2: Load new data from Excel
df = pd.read_excel('data/employee_data.xlsx')

for _, row in df.iterrows():
    Employee.objects.create(
        name=row['name'],
        email=row['email'],
        phone=row['phone'],
        department_id=row['department_id'],  # FK assumed to exist
        date_of_joining=row['date_of_joining'],
        job_title=row['job_title'],
    )

print("✅ New employee data imported successfully.")
