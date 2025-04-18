from django.contrib import admin
from .models import WorkShifts, Attendance

@admin.register(WorkShifts)
class WorkShiftsAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift_type', 'start_time', 'end_time')
    search_fields = ('name', 'shift_type')
    list_filter = ('shift_type',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'shift', 'clock_in', 'clock_out', 'is_present', 'total_hours_worked')
    list_filter = ('is_present', 'shift')
    search_fields = ('employee__name', 'date')
    date_hierarchy = 'date'
    list_per_page = 20  # To limit the number of records per page

    def total_hours_worked(self, obj):
        return obj.total_hours_worked()
    total_hours_worked.short_description = 'Total Hours'
    
    
from django.contrib import admin
from .models import LeaveApproval

@admin.register(LeaveApproval)
class LeaveApprovalAdmin(admin.ModelAdmin):
    list_display = ('leave', 'status', 'approved_by', 'decision_date')
    list_filter = ('status', 'decision_date')
    search_fields = ('leave__employee_id', 'approved_by__username')

