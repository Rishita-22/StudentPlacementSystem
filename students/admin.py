from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'roll_number',
        'department',
        'semester',
        'cgpa'
    ]

    search_fields = [
        'name',
        'roll_number'
    ]

    list_filter = [
        'department',
        'semester'
    ]

    ordering = ['name']