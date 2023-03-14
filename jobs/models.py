from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


# Create your models here.
class JobListing(models.Model):
    company_name = models.CharField(max_length=255)
    job_profile = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    salary = MoneyField(max_digits=10, decimal_places=2, default_currency='INR')
    job_description = models.TextField()
    last_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name + "|" + self.job_profile


class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Unknown')
    email = models.EmailField(default='Unknown')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.job_listing.job_profile}'