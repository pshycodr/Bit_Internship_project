from django.shortcuts import render, redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

# Create your views here.

#  For Authentication
firebaseConfig = {
  "apiKey": "AIzaSyA8P2BGbRuJz8Nz_goXxGmdutsgmI670PI",
  "authDomain": "testy-64346.firebaseapp.com",
  "projectId": "testy-64346",
  "storageBucket": "testy-64346.appspot.com",
  "messagingSenderId": "448793626916",
  "appId": "1:448793626916:web:5adbb1413560821d468bb1",
  "measurementId": "G-9090BKGJD0",
   "databaseURL": "https://testy-64346-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(firebaseConfig)     
auth = firebase.auth()


#  For Firestore
storejson={
  "type": "service_account",
  "project_id": "testy-64346",
  "private_key_id": "7daa90c5ad9f0384fa9acd9192fa5bd09565f020",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDAAJw5roahS7Wi\ndsvVrrNlbb4aNixgZrynixuI03EsStsSrnkmfC4Gn6IY5e/0KWJKvT1zS58eUOtx\nWQitxQkEfTy/FJqEftAeSLc9+M0LoyUhukkehuL87qKucgLUMxK5AWtfUE0t1BKj\nx8IpQJcjGQ+AypUtgow1q+6re1z/9hQ53u2eT7EYLNAa6gfAE4IP1EGf02PEGOis\nVSgK22GQg38v+NSrmkN6s+IFwOMnvWawzz1Pzfo20OshHjnuoeLchUy6+lAP3ab5\nsy5S9CKAarUXhLF7URh5z8+55N9NdemEBhRK53pF6FfraLL+sosHzu1LS48n08gt\n5QOGYmHRAgMBAAECggEAFgnb5MkSHgCFNEVDh176q4lJuVN/i38vZ2HRwsZWZrme\n5MmPEWpOlCcNoaL/BH0dkaugGpRTCtVJ+SQ5mUyVCOVhLCOuyseNlvRMyDm/O3c6\nA2GRFAZylorDtJdUmMvV+dNeYj3i5gBCNXdv43FNB9PQEj3ump8x/dUi258Y4S5H\n9XfjLBuL7zoPwkkJ6EyWDGPVZzj1Wc7vc7QBm3m/K+TVGd5Cr6EnUeQsmHhq3our\nSUbCJi1ebSHzMc+21CNe+q3wp+yGNKHo43U6ZI+V87WLicegh5DkhNKnziZ3Nx+H\nKFU46kjJmgaWYaXsSjZYv/Dp1bA7ycGmeiV5kA+qewKBgQD8w6eXytaOgjToEYWW\n5YRVGEcfBqmjZE4EPm7DeYtP31JIy5CKxfoC3J1wcGZwsIfLpCo/R/RQJJMcG+iy\nkzS/S6y0GZaeMhMjGXHOoMHDsjzhyBRyWkSAXfmLQbdT9H/n/zXeww8JflBv73Z0\nGLhOTzv1xv0HqJCY/tMuW5LNxwKBgQDCddR8mtZ23zQowJbitfV6jx0LFK8mw95i\nIs+8B03Vxn7jkgOSRKWLxiSEG8a5FO0F0wLWAxovHchA7lfciteRUJkMaMoSyDG/\niYowUJQxVGGc0LNUIwaRWKC7YZbGA6ufAMsP25tBmglAGZx0fjHPvkBy4Gj0kU0U\nVxM0LmSzpwKBgQCuN2DlQ75cnSxAJAuStQFf8YrbvKjh4HnRfQK1Iqo91CwP1pb6\nv3gRzuOJIz/IPjRqzOz9jue68Wqf/jCGHOZHT65quBRTVypPj/McOzsyWkCSUmid\nZNBANgWQ0Su95xDd487KimFr5q8kZ8WaQYuPFhe60HuIcsuvWDxQgHeP8wKBgQC1\nuBzQMHW38g8xAgA+beGvHSv73eFrrWAUfwl3Ya/31J1hFmLl/eZhvtEC713+OTLh\n3XVp/s4qN3+aReCvRMP7lMDhGs+zS4dJwUL0sWg6zOrG+zSJrI2Hp7XURXb7JhTr\n6nbYI9VrMYHxd72AEymDQ/vAHjuWSG4qUtCsU6phQwKBgQD6fcDglA2CsyeSYJqI\n8aRXQVT1TtRaWen5XWBr8izFDP3uBx8ym5uC3UfGLu+b7CT67XPLYrPRPv1RuH7F\nZb5GNp0jTtrZJUcOLNmcaG63EQnRNgQIvPvJdl6taPUB3otBKVp5/8n9ue8mmW3z\ndmx5AplIUXIQlCX6Qif7xGoMuA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ffkio@testy-64346.iam.gserviceaccount.com",
  "client_id": "111692871858520504757",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ffkio%40testy-64346.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

credq = credentials.Certificate(storejson)
if not firebase_admin._apps:
  firebase_admin.initialize_app(credq)

database = firestore.client()






#  Admin Login
def adminLogin(request):
    
    adEmail = request.POST.get("Admin_UserEmail")
    adPass = request.POST.get("Admin_Password")
    
    try:
        if adEmail == "Administrator007@gmail.com" and adPass == "Administrator007":
            return redirect(request, "teacherSignUp")
    except: 
        print("Invalid Credentials")

    return render(request, "admin.html")




#  Sign Up
def teacherSignUp(request):
    
  name = request.POST.get("signupName")
  phone = request.POST.get("signupNumber")
  email = request.POST.get("signupEmail")
  password = request.POST.get("signupPassword")

  teacher_data = {"Name":name, "Phone Number":phone, "Email id":email, "password":password}
  try:
    auth.create_user_with_email_and_password(email, password) 
    database.collection('Teachers Database').document(email).set(teacher_data)
    print("account creation successful")
    return redirect(request, "teacherLogin")

  except:
    print("something is wrong!!")
    
  return render(request, "signup.html")





#  Login
def teacherLogin(request):
    
  email = request.POST.get("loginEmail")
  password = request.POST.get("loginPassword")

  try:
     auth.sign_in_with_email_and_password(email, password)
     print("login successful")
     return redirect(request, "marks")
  except:
     print("invalid credentials")
  return render(request, 'login.html')



# Input Marks
# def marks(request):
#   name = request.POST.get("student_name")
#   department = request.POST.get("student_department")
#   sem = request.POST.get("student_sem")
#   reg = request.POST.get("regNo")

#   C = request.POST.get("subject1")
#   python = request.POST.get("subject2")
#   cso = request.POST.get("subject3")
#   ds = request.POST.get("subject4")
#   algo = request.POST.get("subject5")

#   student_info = {"Name":name, "Department": department}

#   database.collection('Students Marks').document(reg).set(teacher_data)  

   
#   return render (request, "marks.html")
