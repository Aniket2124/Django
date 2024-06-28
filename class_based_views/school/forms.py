from django import forms
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']

        widgets = {
            'name': forms.TextInput(attrs={'class':'myclass'}),
            'email': forms.EmailInput(attrs={'class':'myemail'}),
            'password': forms.PasswordInput(attrs={'class':'mypass'}),
        }