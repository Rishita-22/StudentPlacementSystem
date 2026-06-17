from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from students.models import StudentProfile

# =========================
# REGISTER VIEW (SAFE)
# =========================
def register_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:

            error = "Passwords do not match"

        elif User.objects.filter(username=username).exists():

            error = "Username already exists"

        else:

            user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        StudentProfile.objects.create(
            user=user
        )

        return redirect('login')

    return render(
        request,
        'accounts/register.html',
        {
            'error': error
        }
    )


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
                return redirect('dashboard')
            else:
                error = "Invalid username or password"

        else:
            error = "Please fill all fields"

    return render(request, 'accounts/login.html', {'error': error})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')