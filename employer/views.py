from django.shortcuts import render
from jobs.models import JobListing
from django.views.generic.edit import CreateView

class CreateNewJob(CreateView):
    model = JobListing
    template_name = "employer/create.html"
    fields = ['company_name', 'job_profile', 'job_location', 'salary', 'job_description', 'last_date']
