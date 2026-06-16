from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import JobPosting
from .forms import JobForm


@login_required
def job_list(request):

    q = request.GET.get('q')

    jobs = JobPosting.objects.all()

    if q:

        jobs = jobs.filter(

            Q(job_title__icontains=q)

            |

            Q(company__company_name__icontains=q)

        )

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs
        }
    )


@login_required
def add_job(request):

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Job added successfully."
            )

            return redirect('job_list')

    else:

        form = JobForm()

    return render(
        request,
        'jobs/add_job.html',
        {
            'form': form
        }
    )

@login_required
def edit_job(request, id):

    job = JobPosting.objects.get(id=id)

    if request.method == 'POST':

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Job updated successfully."
            )

            return redirect('job_list')

    else:

        form = JobForm(
            instance=job
        )

    return render(
        request,
        'jobs/edit_job.html',
        {
            'form': form
        }
    )

@login_required
def delete_job(request, id):

    job = JobPosting.objects.get(id=id)

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            "Job deleted successfully."
        )

        return redirect('job_list')

    return render(
        request,
        'jobs/delete_job.html',
        {
            'job': job
        }
    )