from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    #return HttpResponse("Hello, World! This is a simple Django application.")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("Hello, World! This is a simple About.")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello, World! This is a simple contact.")
    return render(request, 'website/contact.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "website/login.html")



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")  # Redirect to login page after successful registration

    return render(request, "website/register.html")

