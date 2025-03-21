from django.contrib import admin
from .models import Payroll, Bonus, Tax

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'payment_date', 'payment_method')
    search_fields = ('employee__employee_id', 'payment_method')
    list_filter = ('payment_date', 'payment_method')


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'bonus_date', 'reason')
    search_fields = ('employee__employee_id',)
    list_filter = ('bonus_date',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('employee', 'tax_type', 'amount', 'tax_date')
    search_fields = ('employee__employee_id', 'tax_type')
    list_filter = ('tax_date', 'tax_type')
