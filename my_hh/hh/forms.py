from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *


class CreateJobPostingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.employer = kwargs.pop("employer", None)
        super(CreateJobPostingForm, self).__init__(*args, **kwargs)

    title = forms.CharField(label='Title', max_length=500, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}))
    industry = forms.ChoiceField(label='Industry', required=True, choices=JobPosting.INDUSTRY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-select', 'name': 'industry'}))
    country = forms.ChoiceField(label='Country', required=True, choices=JobPosting.COUNTRY_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-select', 'name': 'country'}))
    city = forms.CharField(label='City', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city'}))
    job_description = forms.CharField(label='Describe the job', required=True,
                                 widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'name': 'job_description'}))
    experience_required = forms.CharField(label='Job requirements', required=True,
                                 widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'name': 'experience_required'}))
    does_not_need_experience = forms.BooleanField(label="The job does not require any special experience", required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3', 'name': 'does_not_need_experience'}))
    is_remote = forms.BooleanField(label="This is a remote job", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input ms-3',
                                                                                    'name': 'is_remote'}))
    is_part_time = forms.BooleanField(label="Part-time work possible", required=False,
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