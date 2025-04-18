from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name', 'location')
    search_fields = ('dept_id', 'name', 'location')
    list_filter = ('name',)
    ordering = ('dept_id',)
    readonly_fields = ('dept_id',)  # Prevent manual editing in admin

    def save_model(self, request, obj, form, change):
        # Safely trigger save() method that auto-generates dept_id
        obj.save()
