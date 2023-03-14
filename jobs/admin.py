from django.contrib import admin
from .models import JobListing, JobApplication

# Register your models here.
class JobListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobListing, JobListingAdmin)


class JobApplicationAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobApplication, JobApplicationAdmin)