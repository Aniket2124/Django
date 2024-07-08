from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .forms import SignUpForm, ProfileForm, BlogPost
from .models import Blog
# Create your views here.

def register(request):
    if request.method == 'POST':
        fm = SignUpForm( request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = SignUpForm()
    return render(request,'apps/signup.html',{'form':fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request,'apps/login.html',{'form':fm})



def profile(request):
    if request.method == 'POST':
        fm = ProfileForm(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
    else:
        fm = ProfileForm(instance=request.user)
    return render(request, 'apps/profile.html',{'form':fm})

def user_logout(request):
    logout(request)
    return redirect('/')

#---------------------------------------------------------------------------------


def create_blog(request):
    if request.method == 'POST':
        fm = BlogPost(request.POST, request.FILES)

        if fm.is_valid():
            title = fm.cleaned_data['title']            
            author = fm.cleaned_data['author']            
            content = fm.cleaned_data['content']            
            image = fm.cleaned_data['image']
            
            reg = Blog(title=title, author=author, content=content, image=image )    
            reg.save()
            # fm.save()
            return redirect('success')
    else:
        fm = BlogPost()
    return render(request, 'apps/blog_post.html',{'form':fm})


def success(request):
    return HttpResponse('successfully uploaded')

def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/details/')
    else:
        form = BlogPost(instance=blog)
    return render(request, 'apps/blog_post.html', {'form': form, 'blog': blog})


def blog_details(request):
    blog = Blog.objects.all()
    return render(request, 'apps/blog_detail.html', {'blog':blog})


def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('/details/')
