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

def delete_employee(request, id):
    if request.method == "POST":
        dele = Employee.objects.get(pk=id)
        dele.delete()
        return HttpResponseRedirect('/')

def update_employee(request,id):
    if request.method == 'POST':
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST,instance=emp)
      
        if fm.is_valid():
            fm.save()
    else:
        emp = Employee.objects.get(pk=id)
        fm = EmployeeForm(instance=emp)
    return render(request,'employee_register/update_employee.html',{'form':fm})
