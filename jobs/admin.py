from django.contrib import admin
from .models import JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'title',
        'company',
        'deadline'
    ]

    search_fields = [
        'title'
    ]

    list_filter = [
        'company'
    ]

    ordering = [
        'deadline'
    ]