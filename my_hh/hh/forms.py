from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, ModelChoiceField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from phonenumber_field.modelfields import PhoneNumberField

from .models import *


class CreateJobPostingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.employer = kwargs.pop("employer", None)
        self.initial_industry = kwargs.pop("initial_industry", None)
        super(CreateJobPostingForm, self).__init__(*args, **kwargs)

    title = forms.CharField(label='Title', max_length=500, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}))
    industry = ModelChoiceField(label='Industry', required=True, queryset=Industry.objects.all(),
                                initial=Industry.objects.get_or_create(title="Unspecified")[0],
                                 widget=forms.Select(attrs={'class': 'form-select', 'name': 'industry'}))
    country = forms.ChoiceField(label='Country', required=True, choices=JobPosting.COUNTRY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-select', 'name': 'country', 'id': 'country'}))
    city = forms.CharField(label='City', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city', 'id': 'city'}))
    job_description = forms.CharField(label='Describe the job', required=True,
                                 widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'name': 'job_description'}))
    experience_required = forms.CharField(label='Job requirements', required=True,
                                 widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'name': 'experience_required'}))
    does_not_need_experience = forms.BooleanField(label="The job does not require any special experience", required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3', 'name': 'does_not_need_experience'}))
    is_remote = forms.BooleanField(label="This is a remote job", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3',
                                                                                    'name': 'is_remote'}))
    is_part_time = forms.BooleanField(label="This is a part-time job", required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3',
                                                                                    'name': 'is_part_time'}))
    additional_information = forms.CharField(label='Additional information that you want to provide', required=False,
                                 widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'name': 'additional_information'}))
    min_salary = forms.DecimalField(label="Minimum salary (per month) in roubles", required=True,
                                 widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'min_salary'}))
    max_salary = forms.DecimalField(label="Maximum salary (per month) in roubles", required=True,
                                    widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'max_salary'}))

    class Meta:
        model = JobPosting
        fields = ["title", "industry", "country", "city", "job_description",
                  "experience_required", "does_not_need_experience", "is_remote", "is_part_time", "additional_information",
                  "min_salary", "max_salary"]

    def save(self, commit=True, **kwargs):
        my_form_object = super(CreateJobPostingForm, self).save(commit=False)
        my_form_object.employer = self.employer
        if commit:
            my_form_object.save()
        return my_form_object


class CreateResumeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(CreateResumeForm, self).__init__(*args, **kwargs)

    title = forms.CharField(label='Title', max_length=250, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}))
    first_name = forms.CharField(label='First Name', max_length=150, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
    last_name = forms.CharField(label='First Name', max_length=150, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
    preferred_country = forms.ChoiceField(label='Country', required=True, choices=JobPosting.COUNTRY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-select', 'name': 'country', 'id': 'country'}))
    preferred_location = forms.CharField(label='City', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city', 'id': 'city'}))
    date_of_birth = forms.DateField(label='Date of birth', required=True,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'date_of_birth', 'type': "date"}))
    phone_number = PhoneNumberField()

    class Meta:
        model = Resume
        fields = ["title", 'first_name', 'last_name', 'preferred_country', 'preferred_location', 'date_of_birth', 'phone_number']
        widgets = {
            "phone_number": RegionalPhoneNumberWidget(attrs={'class': 'form-control', 'name': 'phone_number'}),
        }

    def save(self, commit=True, **kwargs):
        my_form_object = super(CreateResumeForm, self).save(commit=False)
        my_form_object.user = self.user
        if commit:
            my_form_object.save()
        return my_form_object


class EditEmployerProfileForm(ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ["telegram_ID", 'company_name', 'company_logo', 'phone_number']
        widgets = {
            "phone_number": RegionalPhoneNumberWidget(attrs={'class': 'form-control', 'name': 'phone_number'}),
            "telegram_ID": forms.TextInput(attrs={'class': 'form-control', 'name': 'telegram_ID'}),
            "company_name": forms.TextInput(attrs={'class': 'form-control', 'name': 'company_name'}),
            "company_logo": forms.TextInput(attrs={'class': 'form-control', 'name': 'company_logo'}),
        }


class EditJobSeekerProfileForm(ModelForm):
    preferred_country = forms.ChoiceField(choices=COUNTRY_CHOICES,
                                          widget=forms.Select(attrs={'class': 'form-select', 'name': 'country', 'id': 'country'}))

    class Meta:
        model = JobSeekerProfile
        fields = ["image", "phone_number", "telegram_ID", "preferred_country", "preferred_location", "preferred_industry"]
        widgets = {
            "phone_number": RegionalPhoneNumberWidget(attrs={'class': 'form-control', 'name': 'phone_number'}),
            "image": forms.URLInput(attrs={'class': 'form-control', 'name': 'image'}),
            "telegram_ID": forms.TextInput(attrs={'class': 'form-control', 'name': 'telegram_ID'}),
            "preferred_location": forms.TextInput(attrs={'class': 'form-control', 'name': 'city', 'id': 'city'}),
            "preferred_industry": forms.Select(attrs={'class': 'form-select', 'name': 'industry'}),
        }