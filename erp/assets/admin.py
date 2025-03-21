from django.contrib import admin
from .models import Asset, Assignment

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'category', 'purchase_date', 'status')
    list_filter = ('category', 'status')
    search_fields = ('asset_name', 'category')
    ordering = ('purchase_date',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'assigned_date', 'return_date')
    list_filter = ('assigned_date', 'return_date')
    search_fields = ('asset__asset_name', 'employee__employee_id')
    ordering = ('assigned_date',)
