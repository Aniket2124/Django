from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def addshow(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentForm()

    else:
        fm = StudentForm()
    stud = Student.objects.all()
    return render(request, 'student/add_show.html',{'form':fm, 'stu':stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

def update_data(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentForm(instance=pi)

    return render(request, 'student/update_student.html',{'form':fm})