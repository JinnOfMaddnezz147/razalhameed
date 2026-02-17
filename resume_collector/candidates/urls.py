# candidates/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('', views.candidate_list, name='candidate_list'),
]