# tasks/urls.py
from django.urls import path
from .views import punch_in, punch_out, work_summary

urlpatterns = [
    path('punch-in/', punch_in, name='punch_in'),
    path('punch-out/', punch_out, name='punch_out'),
    path('work-summary/', work_summary, name='work_summary'),
]
