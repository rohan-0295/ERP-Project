# Generated by Django 5.1.7 on 2025-04-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
