# Generated by Django 5.1.7 on 2025-04-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_employeeprofile_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveFulltimeEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('full_name', models.CharField(max_length=255)),
                ('department_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'active_fulltime_employees',
                'managed': False,
            },
        ),
    ]
