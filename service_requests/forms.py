from django import forms
from .models import ServiceRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details', 'attached_file']
        widgets = {
            'service_type': forms.TextInput(attrs={
                'class': 'form-control shadow-sm',
                'placeholder': 'Enter service type',
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-control shadow-sm',
                'rows': 5,
                'placeholder': 'Enter details',
            }),
            'attached_file': forms.FileInput(attrs={
                'class': 'form-control shadow-sm',
            }),
        }
