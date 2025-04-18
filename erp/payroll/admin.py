from django.contrib import admin
from .models import Payroll, Bonus, Tax

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'gross_salary', 'net_salary', 'payment_date', 'payment_method')  # Added net_salary
    search_fields = ('employee__employee_id', 'payment_method')
    list_filter = ('payment_date', 'payment_method')

    # Optional: Add functionality to exclude net_salary from being manually edited in the form
    readonly_fields = ('net_salary',)  # Make net_salary readonly since it's calculated by trigger

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'bonus_date', 'reason')
    search_fields = ('employee__employee_id',)
    list_filter = ('bonus_date',)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('employee', 'tax_type', 'tax_percentage', 'tax_date')  # Added tax_percentage
    search_fields = ('employee__employee_id', 'tax_type')
    list_filter = ('tax_date', 'tax_type')
    
    
# payroll/admin.py

from .models import EmployeeSalaryView

@admin.register(EmployeeSalaryView)
class EmployeeSalaryViewAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'job_title', 'gross_salary', 'tax_percentage', 'total_bonus', 'net_salary')

