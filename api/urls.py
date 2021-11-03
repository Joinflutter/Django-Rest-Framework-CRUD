from django.urls import path
from .views import *

urlpatterns = [
    path('students_list/', students_list, name='students_list'),
    path('students_detail/<str:pk>/', students_detail, name='students_detail'),
    path('student_create/', student_create, name='student_create'),
    path('student_delete/<str:pk>', student_delete, name='student_delete'),
    path('student_update/<str:pk>', student_update, name='student_update'),
]