from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

from .models import *
from .forms import *


def index(request):
    context = {}
    if request.user.is_authenticated:
        job_postings = JobPosting.objects.all()
        context = {'job_postings' : job_postings}

        #loading index page for employer
        if request.user.is_employer:
            pass

        # loading index page for job seeker
        # job seeker has a city
        elif not request.user.is_employer:
            # job seeker has a city
            if request.user.jobseekerprofile.preferred_location:
                jobs_in_location = JobPosting.objects.filter(country=request.user.jobseekerprofile.preferred_country,
                                                             city=request.user.jobseekerprofile.preferred_location).order_by(
                                                                "-job_open_date").select_related('industry')[:12]
                industries_gt0_in_location = Industry.objects.annotate(cnt_jobpostings=Count('jobposting')).filter(
                                                cnt_jobpostings__gt=0, jobposting__country=request.user.jobseekerprofile.preferred_country,
                                                jobposting__city=request.user.jobseekerprofile.preferred_location)
                if jobs_in_location:
                    context.update({'jobs_in_location': jobs_in_location})
                if industries_gt0_in_location:
                    context.update({'industries_gt0_in_location': industries_gt0_in_location})
            # job seeker does not have a city
            elif not request.user.jobseekerprofile.preferred_location:
                jobs_in_location = JobPosting.objects.all().order_by(
                                    "-job_open_date").select_related('industry')[:12]
                industries_gt0_in_location = Industry.objects.annotate(cnt_jobpostings=Count('jobposting')).filter(
                                                cnt_jobpostings__gt=0)
                if jobs_in_location:
                    context.update({'jobs_in_location': jobs_in_location})
                if industries_gt0_in_location:
                    context.update({'industries_gt0_in_location': industries_gt0_in_location})
    return render(request, "hh/index.html", context)


@login_required
def job_posting_view(request, job_posting_uuid):
    try:
        job_posting = JobPosting.objects.get(id=job_posting_uuid)
    except ObjectDoesNotExist:
        raise Http404
    context = {'job_posting': job_posting}
    return render(request, "hh/job_posting.html", context)


@login_required
def create_job_posting_view(request):

    # Only an employer account allowed on the page
    if not request.user.is_employer:
        raise PermissionDenied()

    # Creating a new job posting using a form
    form = CreateJobPostingForm(request.POST or None)
    if request.method == 'POST':
        form = CreateJobPostingForm(request.POST, employer=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posting successfully created.")
            return redirect('index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    context = {'form': form}
    return render(request, "hh/create_job_posting.html", context)


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


def register_view(request):
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
            messages.error(request, "Username already taken")
            return render(request, "hh/register.html")

        # Creating additional profile
        if user.is_employer:
            new_profile = EmployerProfile.objects.get_or_create(
                user=user,
                company_name=request.POST.get('company_name', None),
                company_logo=request.POST.get('company_logo', None),
                telegram_ID=request.POST.get('telegram_ID', None),
                phone_number=request.POST.get('phone_number', None),
            )
            new_profile[0].save()
        else:
            new_profile = JobSeekerProfile.objects.get_or_create(
                user=user,
                image=request.POST.get('photo', None),
                telegram_ID=request.POST.get('telegram_ID', None),
                phone_number=request.POST.get('phone_number', None),
                gender=request.POST.get('gender', None),
                preferred_country=request.POST.get('country', None),
                preferred_location=request.POST.get('city', None),
            )
            new_profile[0].save()
        login(request, user)
        messages.success(request, "Welcome!")
        return HttpResponseRedirect(reverse("index"))
    return render(request, "hh/register.html")
