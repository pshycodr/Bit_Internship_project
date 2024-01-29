from django.urls import path
from . import views

urlpatterns=[
    path('teacher-Login/', views.teacherLogin , name= "teacherLogin"),
]