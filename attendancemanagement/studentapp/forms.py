from django import forms
# from .models import Students
class StudentDOB(forms.ModelForm):

    Dob = forms.DateTimeField(
    widget=forms.DateTimeInput(
        attrs={
            "type": 'date',
            "class": 'form-control'
        }
    )
)
