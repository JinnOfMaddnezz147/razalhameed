from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CandidateForm
from .models import Candidate
from django.db.models import Q

def upload_resume(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume submitted successfully!')
            return redirect('candidate_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CandidateForm()

    return render(request, 'candidates/upload.html', {'form': form})


def candidate_list(request):
    candidates = Candidate.objects.all()
    
    # Get filter params from GET request
    skill = request.GET.get('skill', '').strip()
    experience = request.GET.get('experience')
    graduation_year = request.GET.get('graduation_year')
    
    if skill:
        # Simple search: split skills by comma and check if any match
        skill_queries = [Q(skills__icontains=s.strip()) for s in skill.split(',') if s.strip()]
        if skill_queries:
            query = skill_queries.pop()
            for q in skill_queries:
                query |= q
            candidates = candidates.filter(query)
    
    if experience:
        try:
            exp = int(experience)
            candidates = candidates.filter(years_of_experience__gte=exp)
        except ValueError:
            pass  # Ignore invalid input
    
    if graduation_year:
        try:
            year = int(graduation_year)
            candidates = candidates.filter(graduation_year=year)
        except ValueError:
            pass  # Ignore invalid input
    
    return render(request, 'candidates/list.html', {
        'candidates': candidates,
        'current_skill': skill,
        'current_experience': experience,
        'current_graduation_year': graduation_year,
    })