from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'is_employer',)


class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'image', )


class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'company_logo', )


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'industry', 'visible',)


admin.site.register(User, UserAdmin)

admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(JobPosting, JobPostingAdmin)