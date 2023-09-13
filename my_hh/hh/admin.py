from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'is_employer',)


class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'image', 'phone_number', 'telegram_ID')

admin.site.register(User, UserAdmin)
admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)