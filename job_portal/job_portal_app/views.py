from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main/user/main_page.html')

def profile(request):
    return render(request, 'main/user/profile_page.html')


def job_alert(request):
    return render(request, 'main/user/job_alert_page.html')

def main_company(request):
    return render(request, 'main/company/main_page.html')

def add_job(request):
    return render(request, 'main/company/add_job_page.html')

def profile_company(request):
    return render(request, 'main/company/profile_page.html')

def main_admin(request):
    return render(request, 'main/admin/main_page.html')

def job_seeker(request):
    return render(request, 'main/admin/job_seeker_page.html')

def company(request):
    return render(request, 'main/admin/company_page.html')

def job_application(request):
    return render(request, 'main/admin/job_application_page.html')
