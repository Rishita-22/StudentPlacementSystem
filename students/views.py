from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Student
from .forms import StudentForm
from departments.models import Department


@login_required
def student_list(request):

    q = request.GET.get('q')
    department_id = request.GET.get('department')

    students = Student.objects.all()

    # SEARCH
    if q:
        students = students.filter(name__icontains=q)

    # FILTER
    if department_id:
        students = students.filter(department_id=department_id)

    departments = Department.objects.all()

    # -----------------------------
    # PAGINATION (ADDED PART)
    # -----------------------------
    from django.core.paginator import Paginator

    paginator = Paginator(students, 10)  # 10 per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(
        request,
        'students/student_list.html',
        {
            'students': students,
            'departments': departments
        }
    )
    
@login_required
def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student added successfully."
            )

            return redirect('student_list')

    else:

        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {
            'form': form
        }
    )

@login_required
def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student updated successfully."
            )

            return redirect('student_list')
    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/edit_student.html',
        {
            'form': form
        }
    )

@login_required
def delete_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        student.delete()

        messages.success(
            request,
            "Student deleted successfully."
        )

        return redirect('student_list')

    return render(
        request,
        'students/delete_student.html',
        {
            'student': student
        }
    )