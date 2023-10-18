from django import forms
from .models import JobPost,Consultant

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['name','job_title','company_name','company_email','mobile_number','job_description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Company Email'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Job Description'}),
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model= Consultant
        fields=['name','email_id','phone_number','comment']