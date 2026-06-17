from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Company
from .forms import CompanyForm


@login_required
def company_list(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    q = request.GET.get('q')

    companies = Company.objects.all()

    if q:

        companies = companies.filter(
            company_name__icontains=q
        )

    return render(
        request,
        'companies/company_list.html',
        {
            'companies': companies
        }
    )
    

@login_required
def add_company(request):

    if not request.user.is_staff:
        return redirect('dashboard')

    if request.method == 'POST':

        form = CompanyForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company added successfully."
            )

            return redirect('company_list')

    else:

        form = CompanyForm()

    return render(
        request,
        'companies/add_company.html',
        {
            'form': form
        }
    )


@login_required
def edit_company(request, id):

    if not request.user.is_staff:
        return redirect('dashboard')

    company = Company.objects.get(id=id)

    if request.method == 'POST':

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect('company_list')

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        'companies/edit_company.html',
        {
            'form': form
        }
    )


@login_required
def delete_company(request, id):

    if not request.user.is_staff:
        return redirect('dashboard')

    company = Company.objects.get(id=id)

    if request.method == 'POST':

        company.delete()

        messages.success(
            request,
            "Company deleted successfully."
        )

        return redirect('company_list')

    return render(
        request,
        'companies/delete_company.html',
        {
            'company': company
        }
    )