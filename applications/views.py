from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Application
from .forms import ApplicationForm


@login_required
def application_list(request):

    q = request.GET.get('q')

    status = request.GET.get('status')

    applications = Application.objects.all()

    if q:

        applications = applications.filter(
            student__name__icontains=q
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