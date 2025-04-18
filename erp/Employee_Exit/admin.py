from django.contrib import admin
from .models import EmployeeExit

class EmployeeExitAdmin(admin.ModelAdmin):
    list_display = ['employee', 'exit_type', 'exit_date', 'last_working_day', 'exit_interview_conducted', 'assets_returned', 'clearance_completed']
    list_filter = ['exit_type', 'exit_date', 'exit_interview_conducted']
    search_fields = ['employee__first_name', 'employee__last_name', 'exit_reason']
    ordering = ['exit_date']

admin.site.register(EmployeeExit, EmployeeExitAdmin)
