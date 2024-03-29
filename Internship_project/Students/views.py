from django.shortcuts import render, redirect
import pyrebase

import firebase_admin
from firebase_admin import credentials, firestore

from fpdf import FPDF
import datetime


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

# Create your views here.

# Student Registration
def register(request):
    stdname = request.POST.get("studentName")
    stdroll = request.POST.get("studentRoll")
    stddept = request.POST.get("student_department")
    stdsem = request.POST.get("student_sem")
    stdphone =request.POST.get("studentNumber")
    stdemail = request.POST.get("studentEmail")
    stdpassword = request.POST.get("studentPassword")

    stdreg_num = str(stdphone)[:4] + str(stdemail)[:4] + str(stdpassword)[:4] + str(stddept)

    student_data = {
    "Name": stdname,
    "Roll": stdroll,
    "Department": stddept,
    "Semester": stdsem,
    "Phone": stdphone,
    "Email": stdemail,
    "Password": stdpassword,
    "Registration Number": stdreg_num,
    }
    try:
        auth.create_user_with_email_and_password(stdemail, stdpassword) 
        database.collection('Students Database').document(stdreg_num).set(student_data)
        print("account creation successful")
        print(f"Reg no. : {stdreg_num}")
        return redirect("/student/get-result/")

    except:
        print("something is wrong!!")


    return render (request, "register.html")



# Input Reg no.
def inputReg(request):
    regNo = request.POST.get("regNo")

    
    print(f" this is {regNo}")
    print(type(regNo))
    
    try:
        data = database.collection('Students Marks').document(regNo).get().to_dict()
        print(type(data))
        print("data comming")

        if data:
            total_marks = sum(int(data['Marks'][subject]) for subject in ['C_programming', 'CSO', 'Python', 'Algorithm', 'Data_Structure'])
            avg_marks = total_marks / 5

            c_g = grade(int(data['Marks']['C_programming']))
            py_g = grade(int(data['Marks']['Python']))
            cso_g = grade(int(data['Marks']['CSO']))
            ds_g = grade(int(data['Marks']['Data_Structure']))
            al_g = grade(int(data['Marks']['Algorithm']))

            m_g = grade(avg_marks)

            result_data = {
                'data': data,
                'cso_g': cso_g,
                'py_g': py_g,
                'c_g': c_g,
                'al_g': al_g,
                'ds_g': ds_g,
                'm_g': m_g,
                'total': total_marks
            }
            print(result_data)
            return render (request, "result.html", {'result_data':result_data})

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"No data found for Reg No. {regNo}")

    return render(request, "reg_no.html")











# Avg of numbers
def grade(avg):
    stat = ''

    if avg >= 91 and avg <= 100:
        stat = "AA"
    elif avg >= 81 and avg < 91:
        stat = "A"
    elif avg >= 71 and avg < 81:
        stat = "B+"
    elif avg >= 61 and avg < 71:
        stat = "B"
    elif avg >= 51 and avg < 61:
        stat = "C+"
    elif avg >= 41 and avg < 51:
        stat = "C"
    elif avg <40: 
        stat = "fail"
    else:
        stat = "Invalid Input!"

    return stat



# pass of fail in each subject
def pf(avg):
    stat= ''
    if avg >= 35:
	    stat = 'P'
    else:
        stat = 'F'

    return stat    




# To make pdf of result
def makepdf(request):

    regNo = request.GET.get("regNo")
    print(f"make pdf {regNo}")
    data = database.collection('Students Marks').document(regNo).get().to_dict()

    if data:
        total_marks = sum(int(data['Marks'][subject]) for subject in ['C_programming', 'CSO', 'Python', 'Algorithm', 'Data_Structure'])
        avg_marks = total_marks / 5

        c_g = grade(int(data['Marks']['C_programming']))
        py_g = grade(int(data['Marks']['Python']))
        cso_g = grade(int(data['Marks']['CSO']))
        ds_g = grade(int(data['Marks']['Data_Structure']))
        al_g = grade(int(data['Marks']['Algorithm']))

        m_g = grade(avg_marks)

        c_pf = pf(int(data['Marks']['C_programming']))
        py_pf = pf(int((data['Marks']['Python'])))
        cso_pf = pf(int((data['Marks']['CSO'])))
        ds_pf = pf(int((data['Marks']['Data_Structure'])))
        al_pf = pf(int((data['Marks']['Algorithm'])))


        pdf = FPDF();
        pdf.add_page()
        pdf.set_font('Arial', '', 16)

        # College Name and Logo
        # pdf.image('icvp.jpg', 10, 8, 25)
        pdf.cell(45, 5, '', 0, 0)
        pdf.cell(159, 5, 'BENGAL INSTITUTE OF TECHNOLOGY', 0, 1)
        pdf.cell(45, 5, '', 0, 1)
        pdf.cell(45, 5, '', 0, 1)

        # Name
        pdf.cell(19,5,'Name:',0,0);
        pdf.cell(100,5,data['Name'],0,0);

        #ROLL NO
        pdf.cell(42,5,'College Roll No:',0,0);
        pdf.cell(22,5,data['Roll'],0,1);
        pdf.cell(22,5,'',0,1);

        #Department
        pdf.cell(25,5,'Stream:',0,0);
        pdf.cell(35,5,data['Department'],0,0);

        #Semester
        pdf.cell(18,5,'Sem:',0,0);
        pdf.cell(40,5,data['Semister'],0,0);

        #COURSE
        pdf.cell(32,5,'Course:',0,0);
        pdf.cell(22,5,'DIPLOMA',0,1);

        # draw line
        pdf.line(20, 45, 210-20, 45,);
        pdf.ln(16);
        pdf.cell(0,0,'',0,1);
        pdf.cell(0,0,'',0,1);


        pdf.cell(100,5,'Subject Name:',0,0);
        pdf.cell(23,5,'Marks',0,0);
        pdf.cell(23,5,'Grade',0,0);
        pdf.cell(13,5,'Status',0,1);
        pdf.cell(10,5,'',0,1);


        pdf.cell(100,5,'C PROGRAMING',0,0);
        pdf.cell(23,5,data['Marks']['C_programming'],0,0);
        pdf.cell(23,5,c_g,0,0);
        pdf.cell(13,5,c_pf,0,1);
        pdf.cell(10,5,'',0,1);

        pdf.cell(100,5,'PYTHON',0,0);
        pdf.cell(23,5,data['Marks']['Python'],0,0);
        pdf.cell(23,5,py_g,0,0);
        pdf.cell(13,5,py_pf,0,1);
        pdf.cell(10,5,'',0,1);


        pdf.cell(100,5,'CSO',0,0);
        pdf.cell(23,5,data['Marks']['CSO'],0,0);
        pdf.cell(23,5,cso_g,0,0);
        pdf.cell(13,5,cso_pf,0,1);
        pdf.cell(10,5,'',0,1);


        pdf.cell(100,5,'DATA STRUCTURE',0,0);
        pdf.cell(23,5,data['Marks']['Data_Structure'],0,0);
        pdf.cell(23,5,ds_g,0,0);
        pdf.cell(13,5,ds_pf,0,1);
        pdf.cell(10,5,'',0,1);

        pdf.cell(100,5,'ALGORITHM',0,0);
        pdf.cell(23,5,data['Marks']['Algorithm'],0,0);
        pdf.cell(23,5,al_g,0,0);
        pdf.cell(13,5,al_pf,0,1);
        pdf.cell(10,5,'',0,1);

        #draw line
        pdf.line(20, 45, 210-20, 45,);
        pdf.ln(2);
        pdf.cell(0,0,'',0,1);
        pdf.cell(0,0,'',0,1);

        pdf.cell(100,5,'Total Marks:',0,0);
        pdf.cell(23,5,str(total_marks),0,1);
        pdf.cell(10,5,'',0,1);
        pdf.cell(100,5,'Average Marks:',0,0);
        pdf.cell(23,5,str(avg_marks),0,1);
        pdf.cell(10,5,'',0,1);
        pdf.cell(100,5,'Grade:',0,0);
        pdf.cell(23,5,m_g ,0,1);

        pdf.cell(100,120,'',0,1);
        pdf.cell(110,5,'This is diigitally signed :',0,0);
        pdf.cell(23,5,str(datetime.datetime.now()),0,0);

        pdf.output(regNo+'.pdf')
        
    return render(request, 'result.html')

