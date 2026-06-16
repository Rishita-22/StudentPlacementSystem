from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'student',
        'job',
        'status',
        'applied_date'
    ]

    search_fields = [
        'student__name'
    ]

    list_filter = [
        'status'
    ]

    ordering = [
        '-applied_date'
    ]