from django import forms
class StudentDOB(forms.ModelForm):

    Dob = forms.DateTimeField(
    widget=forms.DateTimeInput(
        attrs={
            "type": 'date',
            "class": 'form-control'
        }
    )
)
    