from django.urls import path
from user_auth import views

urlpatterns = [
    path('', views.signup,name='signup',),
    path('login/', views.user_login,name='login',),
    path('profile/', views.profile,name='profile',),
    path('logout/', views.user_logout,name='logout',),
    path('change_pass/', views.user_change_pass,name='change_pass',),
    path('change_pass1/', views.user_change_pass1,name='change_pass1',),
]