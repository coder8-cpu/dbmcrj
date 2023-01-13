from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime as dt
from django.core.mail import send_mail
from rest_framework.decorators import api_view,renderer_classes,APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
# views.py for public section

class AllPages():  # rendering the nav bar

    def __init__(self) -> None:
        self.context = {}
    
    def index(self,request):
        if request.method == 'POST':
            data = request.POST
            PublicQueryForm_object = PublicQueryForm()
            PublicQueryForm_object.first_name = data.get('firstname')
            PublicQueryForm_object.last_name = data.get('lastname')
            PublicQueryForm_object.state_name = data.get('state')
            PublicQueryForm_object.query = data.get('subject')
            PublicQueryForm_object.save()
            return redirect(reverse("index"))
        
        self.context['slide_img'] = SliderImage.objects.first()
        self.context['gallary_img'] = PhotoGallary.objects.first()
        self.context['principle_img'] = PrincipleImage.objects.first()
        return render(request,"index.html",self.context)
        
        
    def college(self,request):
        
        return render(request,"college.html")
    
    def academic(self,request):
        data = FacultyMembers.objects.all()
        
        self.context["member"] = data
        
        return render(request,"academic.html",self.context)

    def admission(self,request):
        notice_data = AdmissionNotice.objects.first()
        
        self.context["notice"] = notice_data

        return render(request,"admission.html",self.context)

    def library(self,request):
        lib_data = librarian.objects.first()
        self.context["lib"] = lib_data

        return render(request,"library.html",self.context)

    def faculty(self,request):

        return render(request,"facality.html")

#--------------------index end--------------------------

    def VisionMissionaryGoal(self,request):

        return render(request,"vmg.html")

    def affilation(self,request):

        return render(request,"affilation.html")

    def iqac(self,request):

        return render(request,"IQAC.html")

    def adof(self,request):
        officers_data = AdministrativeOfficer.objects.all()
        self.context['officers'] =  officers_data
        return render(request,"adof.html",self.context)

    def calander(self,request):

        return render(request,"calander.html")

    def cc(self,request):

        return render(request,"cc.html")
    
    def cocourse(self,request):

        return render(request,"cocourse.html")
    
    def cnt(self,request):

        return render(request,"cnt.html")

    def college(self,request):

        return render(request,"college.html")
    def contact(self,request):

        return render(request,"contact.html")
    def depart(self,request):
        dep_data = Courses.objects.all()
        self.context['dep'] = dep_data


        return render(request,"depart.html",self.context)
    def examstr(self,request):

        return render(request,"examstr.html")
    def feestr(self,request):
        fee = course_fee.objects.all()
        self.context["fee"] = fee

        return render(request,"feestre.html",self.context)
    def gbody(self,request):
        g_data = GoverningBody.objects.all()
        self.context["datas"] = g_data
        
        return render(request,"gbdy.html",self.context)
    def mngm(self,request):

        return render(request,"mngm.html")
    def offst(self,request):
        off_data = OfficeStaff.objects.all()
        self.context['off'] = off_data
        return render(request,"offst.html",self.context)
    def res(self,request):

        return render(request,"res.html")
    def rls(self,request):

        return render(request,"rls.html")
    def rules(self,request):

        return render(request,"rulesregulation.html")
    def ser(self,request):

        return render(request,"ser.html")
    def signup(self,request):

        return render(request,"signup.html")
    def stad(self,request):

        return render(request,"stad.html")
    def tc(self,request):
        tc_data = TeachersCouncil.objects.all()
        self.context['tc'] = tc_data
        return render(request,"tc.html",self.context)
    







class allnavs():
    def __init__(self) -> None:
        pass

    def college_nav(self,request,navs):
        if navs =='Vision':
            return redirect(reverse("vision"))
        
        elif navs =='Affilation':
            return redirect(reverse("affilation"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='faculty':
            return redirect(reverse("faculty"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    
    def vision_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='affilation':
            return redirect(reverse("affilation"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    
    def affilation_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
       

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='vmg':
            return redirect(reverse("vision"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass

    def iqac_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='vmg':
            return redirect(reverse("vision"))

        elif navs =='':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        
        elif navs =='aff':
            return redirect(reverse("affilation"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    def gov_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='Vision':
            return redirect(reverse("vision"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        
        elif navs =='Affilation':
            return redirect(reverse("affilation"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    def adm_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='Vision':
            return redirect(reverse("vision"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        
        elif navs =='Affilation':
            return redirect(reverse("affilation"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    def tc_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='Vision':
            return redirect(reverse("vision"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        
        elif navs =='Affilation':
            return redirect(reverse("affilation"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass
    def ofst_nav(self,request,navs):
        if navs =='college':
            return redirect(reverse("college"))
        
        elif navs =='Vision':
            return redirect(reverse("vision"))

        elif navs =='IQAC':
            return redirect(reverse("iqac"))

        elif navs =='/':
            return redirect(reverse("index"))
        
        elif navs =='Affilation':
            return redirect(reverse("affilation"))
        elif navs =='governing':
            return redirect(reverse("gov"))
        elif navs =='admistrative':
            return redirect(reverse("adm"))
        elif navs =='teachers-council':
            return redirect(reverse("tc"))
        elif navs =='officestaff':
            return redirect(reverse("offst"))
        else:
            pass

    def academic_navs(self,request,navs):
        if navs   == 'rules':
            return redirect(reverse("rules"))
        elif navs   == 'calander':
            return redirect(reverse("cal"))
        elif navs   == 'departments':
            return redirect(reverse("dep"))
        elif navs =='/':
            return redirect(reverse("index"))
        else:
        
            pass
    def cal_navs(self,request,navs):
        if navs   == 'rules':
            return redirect(reverse("rules"))
        elif navs   == 'calander':
            return redirect(reverse("cal"))
        elif navs   == 'departments':
            return redirect(reverse("dep"))
        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='academic':
            return redirect(reverse("academic"))
        else:
        
            pass
    def rule_navs(self,request,navs):
        if navs   == 'rules':
            return redirect(reverse("rules"))
        if navs   == 'calander':
            return redirect(reverse("cal"))
        if navs   == 'departments':
            return redirect(reverse("dep"))
        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='academic':
            return redirect(reverse("academic"))
        else:
        
            pass
    def dep_navs(self,request,navs):
        if navs   == 'rules':
            return redirect(reverse("rules"))
        if navs   == 'calander':
            return redirect(reverse("cal"))
        if navs   == 'departments':
            return redirect(reverse("dep"))
        elif navs =='/':
            return redirect(reverse("index"))
        elif navs =='academic':
            return redirect(reverse("academic"))
        else:
            pass
    def admission_navs(self,request,navs):
        if navs =='feestructure':
             return redirect(reverse("fees"))
        elif navs =='carrer-oriented-course':
             return redirect(reverse("carrer"))
        elif navs =='exam-structure':
             return redirect(reverse("exam"))
        elif navs =='/':
             return redirect(reverse("index"))
        elif navs =='admission':
            return redirect(reverse("admission"))
        else:
            pass
    def fees_navs(self,request,navs):
        if navs =='feestructure':
             return redirect(reverse("fees"))
        elif navs =='carrer-oriented-course':
             return redirect(reverse("carrer"))
        elif navs =='exam-structure':
             return redirect(reverse("exam"))
        elif navs =='/':
             return redirect(reverse("index"))
        elif navs =='admission':
            return redirect(reverse("admission"))
        else:
            pass
    def carrer_navs(self,request,navs):
        if navs =='feestructure':
             return redirect(reverse("fees"))
        elif navs =='carrer-oriented-course':
             return redirect(reverse("carrer"))
        elif navs =='exam-structure':
             return redirect(reverse("exam"))
        elif navs =='/':
             return redirect(reverse("index"))
        elif navs =='admission':
            return redirect(reverse("admission"))
        else:
            pass
    def exam_navs(self,request,navs):
        if navs =='feestructure':
             return redirect(reverse("fees"))
        elif navs =='carrer-oriented-course':
             return redirect(reverse("carrer"))
        elif navs =='exam-structure':
             return redirect(reverse("exam"))
        elif navs =='/':
             return redirect(reverse("index"))
        elif navs =='admission':
            return redirect(reverse("admission"))
        else:
            pass

    def library_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))
        elif navs == "/":
            return redirect(reverse("index"))

        else:
            pass
    
    def about_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))
        elif navs == "/":
            return redirect(reverse("index"))
       

        else:
            pass
    def res_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))

        else:
            pass
    def serv_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))

        else:
            pass
    def rules_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))

        else:
            pass
    def management_navs(self,request,navs):
        if navs == 'about':
            return redirect(reverse('about_lib'))

        elif navs == 'resources':
            return redirect(reverse('resources'))

       
        elif navs == 'service':
            return redirect(reverse('service'))

       
        elif navs == 'rules':
            return redirect(reverse('rules_'))

        elif navs == 'Management':
            return redirect(reverse('management'))

        else:
            pass


