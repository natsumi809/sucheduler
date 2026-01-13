from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'color', 'is_all_day')
    list_filter = ('date', 'is_all_day')
    search_fields = ('title',)