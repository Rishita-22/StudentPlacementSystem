from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student
from companies.models import Company
from jobs.models import JobPosting
from applications.models import Application


@login_required
def dashboard(request):

    total_students = Student.objects.count()
    total_companies = Company.objects.count()
    total_jobs = JobPosting.objects.count()
    total_applications = Application.objects.count()

    selected_students = Application.objects.filter(
        status='Selected'
    ).count()

    context = {

        'total_students': total_students,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'selected_students': selected_students
    }

    return render(request, 'dashboard/dashboard.html', context)