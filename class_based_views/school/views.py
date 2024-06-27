from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import School
from django.views.generic import ListView
# Create your views here.

class StudentListView(ListView):
    model = School
    template_name = 'school/student.html'


# for filter
    
    def get_queryset(self):
        return School.objects.filter(course='Python')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fresher'] = School.objects.all().order_by('name')
        return context


#setting your dynamic template
    def get_template_names(self):
        if self.request.COOKIES['user'] == 'Aniket':
            template_name = 'school/aniket.html'
        else:
            template_name = self.template_name
        return [template_name]

    