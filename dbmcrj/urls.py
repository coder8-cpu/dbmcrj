"""dbmcrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from public.views import *
from django.conf import settings
from django.conf.urls.static import static

all         = AllPages()
navs        =  allnavs()
urlpatterns = [
    path('admin/',                         admin.site.urls),
    path("students/",                      include('student.urls')),
    path("query",                          all.index),
    path('',                               all.index, name="index"),
    path('Admission/admission-query/',     all.adm_query, name=""),
    path('contactus/send-contact/',        all.contact, name=""),
    path('newsletter/',                    all.newsletter, name=""),
    path('post/',                          all.index, name=""),
    path('Faculty/',                       all.fac, name="fac"),
    path('Faculty/<navs>/',                navs.college_nav, name=""),
    path('universityresult/',              all.tcsion, name=""),
    path('onlineAdmission/',               all.onlineadmissionadija, name=""),
    
    path('index.html',                     all.index, name="index"),
    path('Admission/',                     all.admission, name="admission"),
    path('Admission/<navs>/',              navs.college_nav, name=""),
    path('Rules/',                         all.rules, name="rules"),
    path('Rules/<navs>/',                  navs.college_nav, name=""),
    path('Department/',                    all.depart, name="dep"),
    path('Department/select/<subject>/',   all.detail_dep, name="dtail_dep"),
    path('Department/select/<subject>/<navs>/',   all.detail_dep, name="dtaildep_nav"),
    path('Department/<navs>/',             navs.college_nav, name=""),
    path('governing-body/',                all.gbody, name="gov"),
    path('governing-body/<navs>/',         navs.college_nav, name=""),
    path('Office-Staff/',                  all.offst, name="off"),
    path('Office-Staff/<navs>/',           navs.college_nav, name=""),
    path('administrative-officers/',       all.admins, name="adm"),
    path('administrative-officers/<navs>/',navs.college_nav, name=""),
    path('contactus/',                     all.contact, name="contact"),
    path('contactus/<navs>/',              navs.college_nav, name=""),
    path('about/',                         all.about, name="about"),
    path('about/<navs>/',                  navs.college_nav, name=""),
    path('gallary/',                       all.gallary, name="gal"),
    path('gallary/<navs>/',                navs.college_nav, name=""),
    path('vision/',                        all.VisionMissionaryGoal, name="vision"),
    path('vision/<navs>/',                 navs.college_nav, name=""),
   
    path('Affilation/',                    all.affilation, name="affilation"),
    path('Affilation/<navs>/',             navs.college_nav, name=""),
    path('iqac/',                          all.iqac, name="iqac"),
    path('iqac/<navs>/',                   navs.college_nav, name=""),
    path('About/',                         all.lib, name="lib_about"),
    path('About/<navs>/',                  navs.college_nav, name=""),
    path('Rules_/',                        all.lib_rules, name="rules_lib"),
    path('Resources/',                     all.res, name="res"),
    path('Resources/<navs>/',              navs.college_nav, name=""),
    path('Rules_/<navs>/',                 navs.college_nav, name=""),
    path('Teachers-Council/',              all.tc, name="tc"),
    path('Teachers-Council/<navs>/',       navs.college_nav, name=""),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
