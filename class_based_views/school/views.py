from django.http import HttpResponse
from django.shortcuts import render
from .models import School, Student
from .forms import ContactForm, StudentForm
from django.views.generic import ListView, DetailView, FormView, CreateView
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

    #--------------------------------------------------------------------------------
class StudentDetailView(DetailView):
    model = School
    template_name = 'school/Stud_detail.html'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_data'] = self.model.objects.all().order_by('id')
        return context
    
#-------------------------------------------------------------------------------------
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


#--------------------------------------------------------------------------------------
# class StudentCreateView(CreateView):
#     model = Student
#     template_name = 'school/create.html'
#     fields = ['name','email','password']
#     # success_url = '/create/'                      #Or you can use get_absolute_url method in models.py to redirect

    # or we can create using form

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/create.html'   
    success_url = '/create/'     