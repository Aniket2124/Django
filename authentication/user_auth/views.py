from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Registered Successfully...!')
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'user_auth/signup.html', {'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully.")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'user_auth/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/profile/')
        else:
            fm = EditUserProfileForm(instance = request.user)
        return render(request,'user_auth/profile.html',{'name':request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_change_pass(request):  
    if request.user.is_authenticated:  
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)       
        return render(request, 'user_auth/user_change_pass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def user_change_pass1(request):  
    if request.user.is_authenticated:  
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)       
        return render(request, 'user_auth/user_change_pass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
    