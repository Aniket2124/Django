from django.urls import path
from apps import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('blog/', views.create_blog, name='blog_post'),
    path('success/', views.success, name='success'),
    path('update/<int:id>/', views.update_blog, name='update'),
    path('details/', views.blog_details, name='details'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
]