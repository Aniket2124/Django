from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee(request):
    if request.method == "POST":
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = EmployeeForm()
    return render(request,'employee_register/add_employee.html',{'form':fm})

def employee_details(request):
    employee = Employee.objects.all()
    return render(request,'employee_register/employee.html',{'emp':employee})