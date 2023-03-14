from django.urls import path
from . import views


app_name = "employer"

urlpatterns = [
    path("new/", views.CreateNewJob.as_view(), name="new_job")
]