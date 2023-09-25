from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'is_employer',)


class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'image', )


class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'company_logo', )


class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'industry', 'employer', 'visible', 'id')


class IndustryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    


admin.site.register(User, UserAdmin)

admin.site.register(JobSeekerProfile, JobSeekerProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Industry, IndustryAdmin)
