from django.shortcuts import render
from django.urls import reverse_lazy  
from django.views import generic  
from .models import Patient


class PatientList(generic.ListView):
    model = Patient
    template_name = "patient/index.html"

class PatientCreate(generic.CreateView):
    model = Patient
    fields = ['name']
    success_url = reverse_lazy('index')

class PatientUpdate(generic.UpdateView):
    model = Patient
    fields = ['name']
    success_url = reverse_lazy('index')

class PatientDelete(generic.DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

class PatientDetail(generic.DetailView):
    model = Patient