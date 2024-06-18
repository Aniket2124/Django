from django.urls import path
from student import views

urlpatterns = [
    path('',views.addshow, name='addshow'),
    path('delete_data/<int:id>/',views.delete_data, name='delete'),
    path('update_data/<int:id>/',views.update_data, name='update'),
]