from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/main/', views.main, name='main'),
    path('user/profile/', views.profile, name='profile'),
    path('user/job_alert/', views.job_alert, name='job_alert'),
    path('company/main/', views.main_company, name='main_company'),
    path('company/add_job/', views.add_job, name='add_job_company'),
    path('company/profile/', views.profile_company, name='profile_company'),
    path('admin/main/', views.main_admin, name='main_admin'),
    path('admin/job_seeker/', views.job_seeker, name='job_seeker'),
    path('admin/company/', views.company, name='company'),
    path('admin/job_application/', views.job_application, name='job_application'),
]