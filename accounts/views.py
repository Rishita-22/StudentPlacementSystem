from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from students.models import Student
from companies.models import Company
from jobs.models import JobPosting
from applications.models import Application


# =========================
# LOGIN VIEW (SAFE)
# =========================
def login_view(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Basic validation
        if username and password:

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = "Invalid username or password"

        else:
            error = "Please fill all fields"

    return render(request, 'accounts/login.html', {'error': error})


# =========================
# DASHBOARD (HOME)
# =========================
@login_required
def home(request):

    total_students = Student.objects.count()
    total_companies = Company.objects.count()
    total_jobs = JobPosting.objects.count()
    total_applications = Application.objects.count()

    selected_students = Application.objects.filter(status='Selected').count()

    context = {
        'total_students': total_students,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'selected_students': selected_students
    }

    return render(request, 'accounts/home.html', context)


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')