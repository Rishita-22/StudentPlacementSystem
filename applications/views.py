from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Application
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404
from students.models import StudentProfile
from jobs.models import JobPosting


@login_required
def application_list(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    q = request.GET.get('q')

    status = request.GET.get('status')

    applications = Application.objects.select_related(
        'student',
        'student__user',
        'job',
        'job__company'
    )

    if q:

        applications = applications.filter(
            student__user__username__icontains=q
        )

    if status:

        applications = applications.filter(
            status=status
        )

    return render(
        request,
        'applications/application_list.html',
        {
            'applications': applications
        }
    )

@login_required
def add_application(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':

        form = ApplicationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Application added successfully."
            )

            return redirect('application_list')

    else:

        form = ApplicationForm()

    return render(
        request,
        'applications/add_application.html',
        {
            'form': form
        }
    )

@login_required
def edit_application(request, id):

    if not request.user.is_staff:
        return redirect('dashboard')

    application = Application.objects.get(id=id)

    if request.method == 'POST':

        form = ApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Application updated successfully."
            )

            return redirect('application_list')

    else:

        form = ApplicationForm(
            instance=application
        )

    return render(
        request,
        'applications/edit_application.html',
        {
            'form': form
        }
    )

@login_required
def delete_application(request, id):

    if not request.user.is_staff:
        return redirect('dashboard')

    application = Application.objects.get(id=id)

    if request.method == 'POST':

        application.delete()

        messages.success(
            request,
            "Application deleted successfully."
        )

        return redirect('application_list')

    return render(
        request,
        'applications/delete_application.html',
        {
            'application': application
        }
    )

@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        JobPosting,
        id=job_id
    )

    student_profile = get_object_or_404(
        StudentProfile,
        user=request.user
    )

    # Prevent duplicate applications
    if not Application.objects.filter(
        student=student_profile,
        job=job
    ).exists():

        Application.objects.create(
            student=student_profile,
            job=job
        )

        messages.success(
            request,
            "Applied successfully."
        )

    else:

        messages.warning(
            request,
            "You have already applied for this job."
        )

    return redirect('job_list')

@login_required
def my_applications(request):

    student_profile = get_object_or_404(
        StudentProfile,
        user=request.user
    )

    applications = Application.objects.filter(
        student=student_profile
    )

    return render(
        request,
        'applications/my_applications.html',
        {
            'applications': applications
        }
    )

@login_required
def update_application_status(
        request,
        id,
        status
    ):

    if not request.user.is_staff:
        return redirect('dashboard')

    application = get_object_or_404(
        Application,
        id=id
    )

    valid_statuses = [
        'Applied',
        'Shortlisted',
        'Selected',
        'Rejected'
    ]

    if status in valid_statuses:

        application.status = status
        application.save()

        messages.success(
            request,
            "Status updated successfully."
        )

    return redirect('application_list')