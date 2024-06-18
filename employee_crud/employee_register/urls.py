from django.urls import path
from employee_register import views
urlpatterns = [
    path('', views.employee_details, name='employee_details'),
    path('add', views.employee, name='employee'),
]