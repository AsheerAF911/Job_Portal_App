from django.urls import path
from . import views
from . views import FilterJobListings


app_name = "jobs"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path('filter/', FilterJobListings.as_view(), name='filter_job_listings'),
]