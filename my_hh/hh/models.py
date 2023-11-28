from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.urls import reverse


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_employer = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class JobPosting(models.Model):
    INDUSTRY_CHOICES = (
        ('1', 'Unspecified'),
        ('2', 'Consulting'),
        ('3', 'Accounting'),
        ('4', 'Finance'),
        ('5', 'Advertising'),
        ('6', 'Human Resources'),
        ('7', 'Sales'),
        ('8', 'News & Media'),
        ('9', 'Insurance'),
        ('10', 'Entertainment'),
        ('11', 'Marketing'),
        ('12', 'Science & Research'),
        ('13', 'Tech'),
        ('14', 'Healthcare'),
        ('15', 'Manufacturing'),
    )
    COUNTRY_CHOICES = (
        ('RU', 'Russia'),
        ('KZ', 'Kazakhstan'),
        ('BY', 'Belarus'),
        ('UZ', 'Uzbekistan'),
        ('AZ', 'Azerbaijan'),
        ('GE', 'Georgia'),
        ('KG', 'Kyrgyzstan'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default='KZ')
    city = models.CharField(max_length=100)
    job_description = models.TextField(max_length=10000)
    additional_information = models.TextField(max_length=10000, null=True, blank=True)
    experience_required = models.CharField(max_length=10000)
    does_not_need_experience = models.BooleanField(default=False)
    is_remote = models.BooleanField(default=False)
    is_part_time = models.BooleanField(default=False)
    employer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='employers')
    job_open_date = models.DateTimeField(auto_now_add=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=2)
    max_salary = models.DecimalField(max_digits=10, decimal_places=2)
    visible = models.BooleanField(default=True)
    liked = models.ManyToManyField('User', blank=True, related_name='liked_posting')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_posting', kwargs={'job_posting_uuid': self.id})


class Industry(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Industries"

    def __str__(self):
        return self.title


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True, verbose_name='Profile image')
    phone_number = PhoneNumberField(null=True, blank=True)
    telegram_ID = models.CharField(max_length=50, null=True, blank=True)
    preferred_country = models.CharField(max_length=100, null=True, blank=True)
    preferred_location = models.CharField(max_length=100, null=True, blank=True)
    preferred_industry = models.CharField(max_length=3, choices=JobPosting.INDUSTRY_CHOICES, default='1')

    def __str__(self):
        return f'{self.user}_profile'


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_ID = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    company_logo = models.URLField(null=True, blank=True, verbose_name='Company logo')
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}_profile'


class Resume(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    first_name = models.CharField(blank=True, max_length=150)
    last_name = models.CharField(blank=True, max_length=150)
    preferred_country = models.CharField(max_length=100, null=True, blank=True)
    preferred_location = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'Resume: {self.title}'

    def get_absolute_url(self):
        return reverse('resume', kwargs={'resume_uuid': self.id})

    def country_name_by_ISO_3166_1_alpha_2_code(self):
        country_dict = {
            'RU': 'Russia',
            'KZ': 'Kazakhstan',
            'BY': 'Belarus',
            'UZ': 'Uzbekistan',
            'AZ': 'Azerbaijan',
            'GE': 'Georgia',
            'KG': 'Kyrgyzstan',
        }
        country = country_dict.get(self.preferred_country, None)
        return country


class ResumeEducationBlock(models.Model):
    uuid = models.CharField(max_length=20, null=True)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='education_blocks')
    educational_institution = models.CharField(max_length=200, null=True, blank=True)
    specialization = models.CharField(max_length=200, null=True, blank=True)
    year_of_graduation = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.now().year)],
            help_text="Please, use the following format: <YYYY>")

    def __str__(self):
        return f'{self.resume} education: {self.educational_institution}'


class ResumeWorkExperienceBlock(models.Model):
    uuid = models.CharField(max_length=20, null=True)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='work_experience_blocks')
    employer = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    employment_began = models.DateField(blank=True, null=True)
    employment_ended = models.DateField(blank=True, null=True)
    job_duties = models.TextField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return f'{self.resume}: {self.employer} - {self.position}'



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """
#     Creates user profile if it does not exist
#     :param sender: User
#     :param instance:
#     :param created:
#     :param kwargs:
#     :return:
#     """
#     if created:
#         if not instance.is_employer:
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
