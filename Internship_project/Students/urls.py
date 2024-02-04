from django.urls import path
from . import views

urlpatterns = [
    path("student-registration/", views.register, name= "student-registration"),
    path("get-result/", views.inputReg, name= "get-result"),
    path('makepdf/',views.makepdf, name = "makepdf"),
]