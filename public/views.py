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

class AllPages():  

    def __init__(self) -> None:
        self.context = {}
    
    def index(self,request):
        if request.method == 'POST':
            data = request.POST
            PublicQueryForm_object = feedback()
            PublicQueryForm_object.name = data.get('name')
            PublicQueryForm_object.msg = data.get('msg')
           
            PublicQueryForm_object.save()
            return redirect(reverse("index"))
        if request.user.is_authenticated:
            self.context['request'] = request.user 

        self.context['slide_img'] = SliderImage.objects.all()
        self.context['gallary_img'] = PhotoGallary.objects.first()
        self.context['mark']      = IndexAlert.objects.all()
        self.context['notice']      = Notice.objects.all()
        self.context['principle'] = PrincipleImage.objects.first()
        self.context['feedback'] = feedback.objects.all()
        
        return render(request,"index.html",self.context)
    def newsletter(self,request):
        data = request.POST
        news = newsletter()
        news.name = data.get('name')
        news.email = data.get('email')
        news.save()
        return redirect(reverse("index"))
    def gallary(self,request):
        return render(request,"gallery.html")
    def admission(self,request):
        notice_data = AdmissionNotice.objects.first()
        
        self.context["notice"] = notice_data

        return render(request,"admission.html",self.context)

    def gbody(self,request):
        g_data = GoverningBody.objects.all()
        self.context["datas"] = g_data
        return render(request,"gbdy.html",self.context)

    def mngm(self,request):
        obj = MamangementMembers.objects.all()
        self.context['obj'] = obj
        return render(request,"mngm.html",self.context)

    def offst(self,request):
        off_data = OfficeStaff.objects.all()
        self.context['off'] = off_data
        return render(request,"offst.html",self.context)

    def res(self,request):
        links = Resource.objects.first()
        books = Book.objects.all()
        ref_books = ReferenceBooks.objects.all()
        self.context['res'] = links
        self.context['book'] = books
        self.context['ref_book'] = ref_books
        return render(request,"res.html",self.context)

    def depart(self,request):
        dep_data = Courses.objects.all()
        notice_data = AdmissionNotice.objects.first()
        self.context['dep'] = dep_data
        self.context["notice"] = notice_data
        return render(request,"department.html",self.context)

    def tc(self,request):
        tc_data = TeachersCouncil.objects.all()
        self.context['tc'] = tc_data
        return render(request,"tc.html",self.context)
    
    def about(self,request):
        
        return render(request,"about.html")
    

    def VisionMissionaryGoal(self,request):

        return render(request,"vision-mission.html")

    def affilation(self,request):

        return render(request,"affilation.html")

    def iqac(self,request):

        return render(request,"iqac.html")

    def contact(self,request):

        return render(request,"contact.html")
    
    def rules(self,request):

        return render(request,"rules.html")
   
    def tc(self,request):
        return render(request,"tc.html")
    
    def admins(self,request):
        return render(request,"adminis.html")
   
    def lib(self,request):
        return render(request,"library.html")
    
    def lib_rules(self,request):
        return render(request,"rules_.html")
    
    def res(self,request):
        return render(request,"res.html")
    def fac(self,request):
        return render(request,"faculty.html")
   
    
    def tcsion(self,request):
        return redirect("https://www.tcsion.com/SelfServices/")
    def onlineadmissionadija(self,request):
        return redirect("https://dbmadmission.aadija.biz/")
   
    


 
class allnavs():
    def __init__(self) -> None:
        pass

    def college_nav(self,request,navs):
        if navs == "about":
            return redirect(reverse("about"))

        if navs == "vision":
            return redirect(reverse("vision"))
        if navs == "Affilation":
            return redirect(reverse("affilation"))

        if navs == "iqac":
            return redirect(reverse("iqac"))

        if navs == "gallary":
            return redirect(reverse("gal"))

        if navs == "contactus":
            return redirect(reverse("contact"))

        if navs == "governing-body":
            return redirect(reverse("gov"))
        if navs == "administrative-officers":
            return redirect(reverse("adm"))
        if navs == "Teachers-Council":
            return redirect(reverse("tc"))
        if navs == "Office-Staff":
            return redirect(reverse("off"))
        if navs == "Rules":
            return redirect(reverse("rules"))
        if navs == "Department":
            return redirect(reverse("dep"))
        if navs == "Admission":
            return redirect(reverse("admission"))
        if navs == "About":
            return redirect(reverse("lib_about"))
        if navs == "Resources":
            return redirect(reverse("res"))
        if navs == "Rules_":
            return redirect(reverse("rules_lib"))
        if navs == "index.html":
            return redirect(reverse("index"))
        if navs == "universityresult":
            return redirect("https://www.tcsion.com/SelfServices/")
        if navs == "onlineAdmission":
            return redirect("https://dbmadmission.aadija.biz/")
        if navs == "NSCB":
            return redirect("/")
        if navs == "Faculty":
            return redirect(reverse("fac"))

    
        