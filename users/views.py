from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import User
from .forms import UserRegisterForm, UserLoginForm

from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Ensure passwords match
        if password != password2:
            messages.error(request, "Passwords do not match")  # ✅ Correct way
            return render(request, "users/register.html", {"is_login": False})

        # Ensure email is unique
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")  # ✅ Correct way
            return render(request, "users/register.html", {"is_login": False})

        # Create the user
        user = User.objects.create_user(email=email, password=password)
        user.save()

        # Log the user in
        login(request, user)
        return redirect("login") 

    return render(request, "users/register.html", {"is_login": False})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # Use built-in form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful! 🎉")  # ✅ Success message
            return redirect("/list")
        else:
            messages.error(request, "Invalid email or password. Please try again.")  # ✅ Error message

    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})



@login_required
def profile_view(request):
    return render(request, "users/profile.html", {"user": request.user})


def logout_view(request):
    logout(request)
    return redirect("login")
