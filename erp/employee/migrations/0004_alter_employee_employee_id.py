# Generated by Django 5.1.7 on 2025-03-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_employee_temp_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
