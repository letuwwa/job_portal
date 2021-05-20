from django import forms
from .models import *


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Введите корректный E-mail'

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'subject',
            'message'
        ]


class JobListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobListingForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].widget.attrs['placeholder'] = 'Minsk,Belarus'
        self.fields['Salary'].widget.attrs['placeholder'] = '500 BYN, 500 USD'
        self.fields['title'].widget.attrs['placeholder'] = 'Software Engineer, Web Designer'
        self.fields['application_deadline'].widget.attrs['placeholder'] = '2020-12-27'

    class Meta:
        model = JobListing
        exclude = ('user', 'image')
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            "file": "CV (pdf format)",
            "name": "Full Name"

        }
