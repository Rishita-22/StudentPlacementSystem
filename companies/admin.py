from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'company_name',
        'eligibility_criteria',
        'package'
    ]

    search_fields = [
        'company_name'
    ]

    ordering = [
        'company_name'
    ]