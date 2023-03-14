from django.views.generic import ListView
from . forms import JobFilterForm, JobApplicationForm
from .models import JobListing, JobApplication
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "jobs/homepage.html"
    model = JobListing
    context_object_name = "jobs"
    paginate_by = 10
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = JobFilterForm(self.request.GET)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = JobFilterForm(self.request.GET)

        if form.is_valid():
            location = form.cleaned_data.get('location')
            if location:
                queryset = queryset.filter(job_location__icontains=location)

        return queryset

class FilterJobListings(ListView):
    model = JobListing
    template_name = "jobs/filter.html"
    context_object_name = "jobs"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query', None)
        location = self.request.GET.get('location', None)
        if search_query:
            queryset = queryset.filter(job_profile__icontains=search_query)
        if location:
            queryset = queryset.filter(job_location=location)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = JobFilterForm(self.request.GET)
        return context


