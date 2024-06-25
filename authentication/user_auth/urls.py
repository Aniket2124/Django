from django.urls import path
from user_auth import views

urlpatterns = [
    path('', views.signup,name='signup',),
    path('login/', views.user_login,name='login',),
    path('profile/', views.profile,name='profile',),
    path('logout/', views.user_logout,name='logout',),
]