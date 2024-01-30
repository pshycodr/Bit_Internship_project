from django.shortcuts import render
import pyrebase

# Create your views here.
firebaseConfig = {
  "apiKey": "AIzaSyA8P2BGbRuJz8Nz_goXxGmdutsgmI670PI",
  "authDomain": "testy-64346.firebaseapp.com",
  "projectId": "testy-64346",
  "storageBucket": "testy-64346.appspot.com",
  "messagingSenderId": "448793626916",
  "appId": "1:448793626916:web:5adbb1413560821d468bb1",
  "measurementId": "G-9090BKGJD0"
}


def teacherLogin(request):

    return render(request, 'marks.html')
