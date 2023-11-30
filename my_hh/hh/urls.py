from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("account/create_job_posting/", views.create_job_posting_view, name='create_job_posting'),
    path("archive_job_posting/<uuid:job_posting_uuid>", views.archive_job_posting, name='archive_job_posting'),
    path("account/my_job_postings/", views.my_job_postings_view, name='my_job_postings'),

    path("account/edit_profile", views.edit_profile_view, name="edit_profile"),
    path("job_posting/<uuid:job_posting_uuid>/", views.job_posting_view, name="job_posting"),
    path('favourite/<uuid:job_posting_uuid>', views.like_job_posting, name='like_job_posting'),
    path('account/favourite_job_postings', views.favourite_job_postings, name='favourite_job_postings'),
    path('account/my_resumes', views.my_resumes_view, name='my_resumes'),
    path('account/search_for_jobs', views.search_for_jobs, name='search_for_jobs'),
    path('account/create_resume', views.create_resume_view, name='create_resume_main'),
    path('account/edit_resume/education/<uuid:resume_uuid>', views.edit_resume_education_view, name='edit_resume_education'),
    path('account/edit_resume/work_experience/<uuid:resume_uuid>', views.edit_resume_work_experience_view, name='edit_resume_work_experience'),
    path('account/edit_resume/main/<uuid:resume_uuid>', views.edit_resume_main_view, name='edit_resume_main'),
    path('resume/<uuid:resume_uuid>', views.resume_view, name='resume'),
    path('resume_delete/<uuid:resume_uuid>', views.delete_resume, name='delete_resume'),
    path("send_resume/<uuid:job_posting_uuid>/<uuid:resume_uuid>", views.send_resume, name="send_resume"),
    ]

