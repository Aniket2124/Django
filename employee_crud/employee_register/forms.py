from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'emp_code': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.Select(attrs={'class':'form-control'})
        }