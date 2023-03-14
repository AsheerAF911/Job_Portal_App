from django import forms
from .models import JobApplication

class JobFilterForm(forms.Form):
    location = forms.CharField(required=False)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'resume', 'cover_letter']