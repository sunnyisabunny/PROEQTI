from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'autocomplete': 'off'}),
        }
