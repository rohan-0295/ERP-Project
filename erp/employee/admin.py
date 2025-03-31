from django.contrib import admin
from .models import Employee, EmployeeProfile
from department.models import Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'job_title', 'get_department', 'employment_type', 'status', 'date_hired')
    search_fields = ('employee_id', 'job_title', 'department__name')
    list_filter = ('employment_type', 'status', 'department', 'job_title')

    def get_department(self, obj):
        # Improved method to handle None values and display department name correctly
        if obj.department:
            return obj.department.name
        return "-"
    get_department.short_description = 'Department'

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'gender', 'get_department')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('gender', 'department')

    def get_department(self, obj):
        # Improved method to handle None values and display department name correctly
        if obj.department:
            return obj.department.name
        return "-"
    get_department.short_description = 'Department'