from django.shortcuts import render

# Create your views here.

def teacherLogin(request):

    return render(request, 'login.html')
