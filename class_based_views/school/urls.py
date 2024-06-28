from django.urls import path
from school import views
urlpatterns = [
    path('',views.StudentListView.as_view(), name='stu_list'),
    path('detail/<int:pk>/',views.StudentDetailView.as_view(), name='detail'),
    path('contact/',views.ContactFormView.as_view(), name='contact'),
    path('create/',views.StudentCreateView.as_view(), name='create'),
]

