# candidates/forms.py
from django import forms
from .models import Candidate
import os

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name', 'date_of_birth', 'contact_number', 'contact_address',
            'education_qualification', 'graduation_year', 'years_of_experience',
            'skills', 'resume_file'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'contact_address': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Python, Django, JavaScript, etc. (comma-separated)'}),
        }

    def clean_resume_file(self):
        file = self.cleaned_data.get('resume_file')
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            allowed = ['.pdf', '.doc', '.docx']
            if ext not in allowed:
                raise forms.ValidationError("Only PDF, DOC, or DOCX files are allowed.")
            # Optional: add size limit
            if file.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("File size must be under 5MB.")
        return file