from django.contrib import admin
from .models import Employee, EmployeeProfile, ActiveFulltimeEmployee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'get_full_name', 'job_title', 'employment_type', 'status', 'department', 'date_hired')
    list_filter = ('employment_type', 'status', 'job_title', 'department')
    search_fields = ('employee_id', 'employeeprofile__first_name', 'employeeprofile__last_name')
    ordering = ('employee_id',)

    def get_full_name(self, obj):
        return obj.employeeprofile.full_name if hasattr(obj, 'employeeprofile') else 'N/A'
    get_full_name.short_description = 'Full Name'


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'gender', 'get_employee_id')
    search_fields = ('first_name', 'last_name', 'email', 'employee__employee_id')
    ordering = ('first_name',)

    def get_employee_id(self, obj):
        return obj.employee.employee_id if obj.employee else 'Unlinked'
    get_employee_id.short_description = 'Employee ID'


# Optional: Register the unmanaged view model (read-only)
@admin.register(ActiveFulltimeEmployee)
class ActiveFulltimeEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'full_name', 'department_name', 'status')
    search_fields = ('full_name', 'department_name')
    ordering = ('employee_id',)

    def has_add_permission(self, request):
        return False  # Prevent adding records in admin

    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing records in admin

    def has_delete_permission(self, request, obj=None):
        return False  # Prevent deleting records in admin
