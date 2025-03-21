from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('name',)
    readonly_fields = ('dept_id',) 

    def save_model(self, request, obj, form, change):
        if not obj.dept_id:
            prefix = obj.PREFIX_MAP.get(obj.name, 'DEP')
            last_dept = Department.objects.filter(name=obj.name).order_by('-dept_id').first()
            if last_dept:
                last_number = int(last_dept.dept_id[len(prefix):])
                new_number = last_number + 1
            else:
                new_number = 1

            obj.dept_id = f"{prefix}{new_number:03d}"
        super().save_model(request, obj, form, change)


