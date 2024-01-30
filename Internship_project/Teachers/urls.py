from django.urls import path
from . import views

urlpatterns=[
    path('teacher-Login/', views.teacherLogin , name= "teacherLogin"),
    path('teacher-signup/', views.teacherSignUp , name= "teacherSignUp"),
    path('Admin-Login/', views.adminLogin , name= "adminLogin"),
]