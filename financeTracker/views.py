from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import *
from .forms import CreateUserForm
from django.contrib import messages

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was successfully created for" + user)

            return redirect("login")


    context = {"form":form}
    return render(request, "register.html", context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("")

    context = {}
    return render(request, "login.html", context)

def home(request):
    return render(request, "index.html")
