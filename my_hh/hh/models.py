from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_employer = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class JobSeekerProfile(models.Model):
    GENDER_CHOICES = (
        ('P', 'Prefer not to say'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True, verbose_name='Profile image')
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    telegram_ID = models.CharField(max_length=50, null=True, blank=True)


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_ID = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    company_logo = models.URLField(null=True, blank=True, verbose_name='Company logo')
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_employer:
#             EmployerProfile.objects.get_or_create(user=instance)
#         else:
#             JobSeekerProfile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()