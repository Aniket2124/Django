from django.urls import path
from api import views

urlpatterns = [
    path('',views.student_api, name='student'),
    path('student_api/<int:pk>/',views.student_api, name='stu_api'),
    path('student/<int:pk>/',views.StudentApiView.as_view(), name='stu'),
]