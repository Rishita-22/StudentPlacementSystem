from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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