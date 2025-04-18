from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, EmployeeProfile

@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and not EmployeeProfile.objects.filter(employee=instance).exists():
        EmployeeProfile.objects.create(
            employee=instance,
            first_name='First',
            last_name='Last',
            email=f'{instance.employee_id.lower()}@company.com'
        )

@receiver(post_save, sender=Employee)
def save_employee_profile(sender, instance, **kwargs):
    if hasattr(instance, 'employeeprofile'):
        instance.employeeprofile.save()
