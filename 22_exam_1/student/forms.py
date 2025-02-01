from django import forms
from . import models


class StudentFrom(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['fullname', 'email', 'course', 'number', 'photo']
        labels = {
            'fullname': 'Enter your Full Name',
            'email': 'Enter your Email Address',
            'course': 'Enter your Course Name',
            'number': 'Enter your Number',
            'photo': 'Upload your Photo'
        }