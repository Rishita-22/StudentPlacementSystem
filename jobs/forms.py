from django import forms
from .models import JobPosting


class JobForm(forms.ModelForm):

    class Meta:

        model = JobPosting

        fields = [
            'company',
            'title',
            'description',
            'deadline'
        ]