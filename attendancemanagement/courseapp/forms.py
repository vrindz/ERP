from django import forms

class BatchForm(forms.ModelForm):
    start_date= forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": 'datetime-local',
                "class": 'form-control'
            }
        )
    )

    end_date=forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": 'date',
                "class": 'form-control'
            }
        )
    )