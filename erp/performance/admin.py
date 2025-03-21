from django.contrib import admin
from .models import Review, Goal

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('employee', 'review_date', 'score', 'comments')
    list_filter = ('review_date', 'score')
    search_fields = ('employee__employee_id', 'employee__job_title')
    ordering = ('review_date',)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('employee', 'description', 'target_date', 'status')
    list_filter = ('status', 'target_date')
    search_fields = ('employee__employee_id', 'description')
    ordering = ('target_date',)
