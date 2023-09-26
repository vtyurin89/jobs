from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("account/create_job_posting/", views.create_job_posting_view, name='create_job_posting'),
    path("job_posting/<uuid:job_posting_uuid>/", views.job_posting_view, name="job_posting"),
    path('favourite/<uuid:job_posting_uuid>', views.like_job_posting, name='like_job_posting'),
    ]

