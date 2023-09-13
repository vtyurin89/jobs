from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError

from .models import *

def index(request):
    return render(request, "hh/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if successful authentication
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hh/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "hh/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == 'POST':

        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords don't match")
            return render(request, "hh/register.html")
        is_employer = True if request.POST["user_type"] == 'employer' else False

        # Creating the new user
        try:
            user = User.objects.create_user(username, email, password)
            user.is_employer = is_employer
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "hh/register.html", {
                "message": "Username already taken."
            })

        # Creating additional profile
        if user.is_employer:
            new_profile = EmployerProfile.objects.create(
                user=user,
                company_name=request.POST['company_name'],
                company_logo=request.POST['company_logo'],
                telegram_ID=request.POST['telegram_ID'],
                phone_number=request.POST['phone_number'],
            )
            new_profile.save()
        else:
            new_profile = JobSeekerProfile.objects.create(
                user=user,
                image=request.POST['photo'],
                telegram_ID=request.POST['telegram_ID'],
                phone_number=request.POST['phone_number'],
                gender=request.POST['gender'],
            )
            new_profile.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "hh/register.html")
