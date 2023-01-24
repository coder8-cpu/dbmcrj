from django.shortcuts import render,redirect
from student.models import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from dbmcrj import settings
import requests
import datetime as dt
from public.models import notice_files


# Create your views here.\


class Dashboard():
    def __init__(self) -> None:
        self.studentname = None
        self.today_routine = None
        self.notifications = None
        self.chats         = None
        self.examnotifications = None
        self.registrationno = None
        self.admit = None
        self.marksheet =None
        self.routine = None
        self.day = None
        self.context = {}
    def show_dashboard(self,request):
        if request.user.is_authenticated:
            d = dt.datetime.now()
            dee = dt.date.today()
        
            data = {"0":"Monday","1":"Tuesday","2":"Wednesday","3":"Thursday","4":"Friday","5":"Saturday","6":"Sunday"}
            for i in data.keys():
            
                if str(i) == str(d.weekday()):
                    self.day = data.get(i)
            print(self.day)
            self.studentname = StudentData.objects.get(rollno=request.session.get('user'))
            self.routine = routine.objects.filter(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,day=self.day)
            self.notifications = notice_files.objects.all()
            self.marksheet = Marksheets.objects.get(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,roll=request.session.get('user'))
            self.registrationno = Registration.objects.get(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,roll=request.session.get('user'))
            self.admit = AdmitCard.objects.get(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,roll=request.session.get('user'))
            self.exam = ExamRoutine.objects.get(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,)
            self.syl = Syllabus.objects.get(year=dt.date.today().year,course_type=self.studentname.course_type,semester=self.studentname.semester,branch=self.studentname.branch,)
            lenght = self.notifications.count()
            self.context["routine"] = self.routine
            self.context["day"] = self.day
            self.context["dee"] = dee
            self.context["lenght"] = lenght
            self.context["marksheet"] = self.marksheet
            self.context["reg"] = self.registrationno
            self.context["admit"] = self.admit
            self.context["sem"] = self.marksheet.semester
            self.context["syl"] = self.syl
            self.context["exam"] = self.exam
            self.context["notifications"] = self.notifications
            self.context["name"] = self.studentname.name
            self.context["branch"] = self.studentname.branch
            self.context["year"] = self.studentname.year
            return render(request,"final.html",self.context)
        return redirect(reverse("index"))
   
def home(request):
    return redirect(reverse("index"))

class geo_locate:
    def __init__(self):
        self.lati             = None
        self.longi            = None
        self.ip               = None


    def get_ip(self,request):
        get_ip                = request.META.get('HTTP_X_FORWARDED_FOR')
        if get_ip:
            self.ip           = get_ip.split(',')[0]
        else:
            self.ip           = request.META.get('REMOTE_ADDR')
        return self.ip


    def get_lat_long(self,request,ip=get_ip):
        get_ip                 = ip(self,request)
        api_key                = settings.GEO_LOCATION_KEY
        response               = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key="+api_key+"&ip_address="+get_ip)
        print(response)
        return redirect(reverse("dashboard"))

class Signup():
    def __init__(self) -> None:
        pass
    def show_signup(self,request):
        return render(request,"signup.html")
    def createuser(self,request):
        data = request.POST
        roll = RegisterRollNo.objects.filter(name=data.get('roll'))
        if roll.exists():
            signup_data = StudentSignup()
            signup_data.name = data.get('name')
            signup_data.Rollno = data.get('roll')
            signup_data.password = make_password(data.get('password'))
            signup_data.save()
            user = User()
            user.username = data.get('roll')
            user.set_password = data.get('password')
            user.save()
            return redirect(reverse("login"))
        else:
            messages.info(request,'The given Roll No is not found in our database')
            return redirect(reverse("signup"))

    def redirect_signup(self,request):
        return redirect(reverse("signup"))
    def redirect_login(self,request):
        return redirect(reverse("login"))

class Login():
    def __init__(self) -> None:
        pass
    def show_login(self,request):
        if request.user.is_authenticated:
            return redirect(reverse("dashboard"))
        return render(request,"login.html")

    def verify_login(self,request):
        data = request.POST
        user = authenticate(username=data.get('roll'),password=data.get('password'))
        if user is not None:
            auth.login(request,user)
            request.session['user'] = data.get('roll')
            return redirect(reverse("dashboard"))
        else:
            messages.info(request,"invalid cerdentials")
            return redirect(reverse("login"))


def logout(request):
    auth.logout(request)
    return redirect(reverse("index"))
        


    
    