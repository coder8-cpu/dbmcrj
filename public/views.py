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
            PublicQueryForm_object      = feedback()
            PublicQueryForm_object.name = data.get('name')
            PublicQueryForm_object.msg  = data.get('msg')
            PublicQueryForm_object.save()
            return redirect(reverse("index"))

        if request.user.is_authenticated:
            self.context['request'] = request.user 
        else:
            self.context['request'] = "Login"

        self.context['slide_img'] = SliderImage.objects.all()
        self.context['slide'] = IndexSliderImage.objects.all()
        self.context['mark']      = IndexAlert.objects.all()
        self.context['notice']    = Notice.objects.all()
        self.context['principle'] = PrincipleImage.objects.first()
        self.context['feedback']  = feedback.objects.all()
        self.context['comp']  = ComputerCenter.objects.first()
        self.context['can']  = Canteen.objects.first()
        
        return render(request,"index.html",self.context)
    def newsletter(self,request):

        data       = request.POST
        news       = newsletter()
        news.name  = data.get('name')
        news.email = data.get('email')
        news.save()
        return redirect(reverse("index"))

    def gallary(self,request):

        self.context['gallary_img'] = PhotoGallary.objects.all()
        return render(request,"gallery.html",self.context)

    def admission(self,request):

        notice_data            = AdmissionNotice.objects.first()
        courses                = CoursesFee.objects.all()
        docs                   = DocumentRequired.objects.all()
        notice_file            = notice_files.objects.all()
        self.context["notice"] = notice_data
        self.context["course"] = courses
        self.context["doc"]    = docs
        self.context["files"]  = notice_file
        return render(request,"admission.html",self.context)

    def adm_query(self,request):

        obj         = PublicQueryForm()
        data        = request.POST
        obj.name    = data.get('name')
        obj.email   = data.get('email')
        obj.subject = data.get('mobileno')
        obj.query   = data.get('message')
        obj.save()
        return redirect(reverse("admission"))

    def gbody(self,request):

        g_data                = GoverningBody.objects.all()
        self.context["datas"] = g_data
        return render(request,"gbdy.html",self.context)

    def mngm(self,request):
        obj                 = MamangementMembers.objects.all()
        self.context['obj'] = obj
        return render(request,"mngm.html",self.context)

    def offst(self,request):
        off_data            = OfficeStaff.objects.all()
        self.context['off'] = off_data
        return render(request,"offst.html",self.context)

    def res(self,request):
        links                    = Resource.objects.first()
        books                    = Book.objects.all()
        ref_books                = ReferenceBooks.objects.all()
        self.context['res']      = links
        self.context['book']     = books
        self.context['ref_book'] = ref_books
        return render(request,"res.html",self.context)

    def depart(self,request):
        dep_data            = Courses.objects.all()
        
        self.context['dep'] = dep_data
        

        return render(request,"department.html",self.context)

    def detail_dep(self,request,subject,navs=None):
        self.currentdep = None
        self.resources  = None
        self.faculty    = None
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

        if subject == "Physics-Honours":
            self.currentdep =  Departments.objects.get(name=subject)
            self.resources =  Eresources.objects.get(departments_id=self.currentdep.id)
            self.faculty =  DepartmentsFaculty.objects.filter(department_id=self.currentdep.id)
            
            self.context['dep'] = self.currentdep
            self.context['faculty'] = self.faculty
            self.context['cure'] = self.resources

            return render(request,"detaildep.html",self.context)
        
        

        
        

    def tc(self,request):
        tc_data            = TeachersCouncil.objects.all()
        self.context['tc'] = tc_data
        return render(request,"tc.html",self.context)
    
    def about(self,request):
        
        return render(request,"about.html")
    

    def VisionMissionaryGoal(self,request):

        return render(request,"vision-mission.html")

    def affilation(self,request):

        return render(request,"affilation.html")

    def iqac(self,request):
        data = IQAC.objects.all()
        aqar = AQAR.objects.all()
        self.context['iqac'] = data
        self.context['aqar'] = aqar
        return render(request,"iqac.html",self.context)

    def contact(self,request):

        if request.method == 'POST':
            data         = PublicQueryForm()
            data.name    = request.POST.get('name')
            data.email   = request.POST.get('email')
            data.subject = request.POST.get('subject')
            data.message = request.POST.get('message')
            return redirect(reverse("contact"))

        return render(request,"contact.html")
    
    def rules(self,request):

        return render(request,"rules.html")
   
    def tc(self,request):
        tc                = TeachersCouncil.objects.all()
        self.context['t'] = tc
        return render(request,"tc.html",self.context)
    
    def admins(self,request):
        datas                = AdministrativeOfficer.objects.all()
        self.context['data'] = datas
        return render(request,"adminis.html",self.context)
   
    def lib(self,request):
        l                   = librarian.objects.first()
        self.context['lib'] = l
        return render(request,"library.html",self.context)
    
    def lib_rules(self,request):
        
        return render(request,"rules_.html")
    
    def res(self,request):
        data                     = Resource.objects.all()
        books                    = Book.objects.all()
        ref_book                 = ReferenceBooks.objects.all()
        self.context['data']     = data
        self.context['ref_book'] = ref_book
        self.context['book']     = books 
        self.context['year']     = currentyear.objects.first()
        return render(request,"res.html",self.context)

    def fac(self,request):
        fac   = FacultyMembers.objects.filter(department="English")
        fac1  = FacultyMembers.objects.filter(department="Bengali")
        fac2  = FacultyMembers.objects.filter(department="Mathematics")
        fac3  = FacultyMembers.objects.filter(department="Physics")
        fac4  = FacultyMembers.objects.filter(department="Chemistry")
        fac5  = FacultyMembers.objects.filter(department="Computer Science")
        fac6  = FacultyMembers.objects.filter(department="Sanskrit")
        fac7  = FacultyMembers.objects.filter(department="Geography")
        fac8  = FacultyMembers.objects.filter(department="Economics")
        fac9  = FacultyMembers.objects.filter(department="Political Science")
        fac10 = FacultyMembers.objects.filter(department="Commerse")
        fac11 = FacultyMembers.objects.filter(department="BBA")
        fac12 = FacultyMembers.objects.filter(department="BCA")
        fac13 = FacultyMembers.objects.filter(department="Philosophy")
        fac14 = FacultyMembers.objects.filter(department="Education")
        fac15 = FacultyMembers.objects.filter(department="Hindi")
        fac16 = FacultyMembers.objects.filter(department="History")
        
        self.context["english"]             = fac
        self.context["Bengali"]             = fac1
        self.context["Mathematics"]         = fac2
        self.context["Physics"]             = fac3
        self.context["Chemistry"]           = fac4
        self.context["ComputerScience"]     = fac5
        self.context["Sanskrit"]            = fac6
        self.context["Geography"]           = fac7
        self.context["Economics"]           = fac8
        self.context["PoliticalScience"]    = fac9
        self.context["Commerse"]            = fac10
        self.context["BBA"]                 = fac11
        self.context["BCA"]                 = fac12
        self.context["Philosophy"]          = fac13
        self.context["Education"]           = fac14
        self.context["Hindi"]               = fac15
        self.context["History"]             = fac16

        return render(request,"faculty.html",self.context)
   
    
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
       

    
        