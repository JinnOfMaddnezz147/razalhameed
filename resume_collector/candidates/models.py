from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    contact_address = models.TextField()
    education_qualification = models.CharField(max_length=255)
    graduation_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(timezone.now().year + 5)
        ]
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    
    # Skills will be stored as comma-separated string (simple approach)
    # Later we can improve to ManyToMany if needed
    skills = models.TextField(
        help_text="Comma-separated list of skills/technologies (e.g. Python, Django, React)"
    )
    
    resume_file = models.FileField(
        upload_to='resumes/%Y/%m/%d/',
        help_text="Upload PDF, DOC, or DOCX only"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.graduation_year})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"