from django.urls import path
from employee_register import views
urlpatterns = [
    path('', views.employee_details, name='employee_details'),
    path('add', views.employee, name='employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
]