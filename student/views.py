from django.shortcuts import render,redirect
from student.models import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Create your views here.\


class Dashboard():
    def __init__(self) -> None:
        pass
    def show_dashboard(self,request):
        return render(request,"dashboard.html")
    def show_marksheet(self,request):
        return render(request,"marksheet.html")
    def show_routine(self,request):
        return render(request,"routine.html")
    def show_admit(self,request):
        return render(request,"admit.html")
    def show_registration(self,request):
        return render(request,"registration.html")
    def show_exams(self,request):
        return render(request,"exam.html")
    def show_sylabus(self,request):
        return render(request,"syl.html")
    def show_notification(self,request):
        return render(request,"notification.html")
    def logout(self,request):
        auth.logout(request)
        return redirect(reverse("index"))
    def dashboard_navs(self,request,navs):
        if navs == "marksheet":
            return redirect(reverse("marksheet"))
        elif navs == "routine":
            return redirect(reverse("routine"))
        elif navs == "admitcard":
            return redirect(reverse("admitcard"))
        elif navs == "syllabus":
            return redirect(reverse("syllabus"))
        elif navs == "registration":
            return redirect(reverse("reg"))
        elif navs == "examschedule":
            return redirect(reverse("exam_schedule"))
        elif navs == "notifications":
            return redirect(reverse("notifications"))
        elif navs == "/":
            return redirect(reverse("index"))
        
        else:
            pass

    

        
        
        
        

    
class Signup():
    def __init__(self) -> None:
        pass
    def show_signup(self,request):
        return render(request,"signup.html")
    def createuser(self,request):
        data = request.POST
        roll = RegisterRollNo.objects.filter(rollno=data.get('rollno'))
        if roll.exists():
            signup_data = StudentSignup()
            signup_data.name = data.get('name')
            signup_data.Rollno = data.get('rollno')
            signup_data.password = make_password(data.get('password'))
            signup_data.save()
            user = User()
            user.username = data.get('rollno')
            user.set_password = data.get('password')
            user.save()
            return redirect(reverse("login"))
        else:
            messages.info(request,'The given Roll No is not found in our database')
            return redirect(reverse("signup"))



class Login():
    def __init__(self) -> None:
        pass
    def show_login(self,request):
        return render(request,"login.html")

    def verify_login(self,request):
        data = request.POST
        user = authenticate(username=data.get('roll'),password=data.get('password'))
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request,"invalid cerdentials")
            return redirect(reverse("login"))



        


    
    