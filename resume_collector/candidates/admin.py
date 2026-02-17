from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'graduation_year',
        'years_of_experience',
        'created_at',
    )
    list_filter = ('graduation_year', 'years_of_experience')
    search_fields = ('full_name', 'skills')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Info', {
            'fields': ('full_name', 'date_of_birth', 'contact_number', 'contact_address')
        }),
        ('Education & Experience', {
            'fields': ('education_qualification', 'graduation_year', 'years_of_experience')
        }),
        ('Skills & Resume', {
            'fields': ('skills', 'resume_file')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )