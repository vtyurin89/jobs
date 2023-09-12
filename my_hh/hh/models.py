from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    is_employer = models.BooleanField(default=False)


class JobSeekerProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True, verbose_name='Profile image')
    phone = PhoneNumberField(null=True, blank=True, unique=True)


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()