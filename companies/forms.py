from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        fields = [
            'company_name',
            'eligibility_criteria',
            'package'
        ]