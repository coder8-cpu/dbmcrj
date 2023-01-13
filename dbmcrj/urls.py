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
from django.urls import path
from public.views import *
from django.conf import settings
from django.conf.urls.static import static

all = AllPages()
navs =  allnavs()
urlpatterns = [
    path('admin/', admin.site.urls),
    path("query",all.index),
    path('',all.index, name="index"),
    path('academic/',all.academic, name="academic"),
    path('admission/',all.admission, name="admission"),
    path('library/',all.library, name="library"),
    path('faculty/',all.faculty, name="faculty"),
    path('college/',all.college, name="college"),

    # inside college nav
    path('Vision-Missionary-Goal/',all.VisionMissionaryGoal, name="vision"),
    path('Vision/',all.VisionMissionaryGoal, name="vision"),
    path('Affilation/',all.affilation, name="affilation"),
    path('IQAC/',all.iqac, name="iqac"),
    path('governing/',all.gbody,name='gov'),
    path('admistrative/',all.adof,name='adm'),
    path('teachers-council/',all.tc,name='tc'),
    path('officestaff',all.offst,name='offst'),

    # inside academic nav
    path('rules/',all.rules,name="rules"),
    path('calandar/',all.calander,name="cal"),
    path('depeartments/',all.depart,name="dep"),

    # inside admission nav
    path('feestructure/',all.feestr,name="fees"),
    path('carrer-oriented-course/',all.cocourse,name="carrer"),
    path('exam-structure/',all.examstr,name="exam"),

    #inside library nav
    path('about/',all.library,name="about_lib"),
    path('resources/',all.res,name="resources"),
    path('services/',all.ser,name="service"),
    path('management/',all.mngm,name="management"),
    path('rules_/',all.rls,name="rules_"),


    
  

    #college navs
    path('college/',all.college, name="college"),
    path('college/<navs>/',navs.college_nav, name="college_nav"),
    path('Vision-Missionary-Goal/<navs>/',navs.vision_nav, name="vision_nav"),
    path('Vision/<navs>/',navs.vision_nav, name="vision_nav"),
    path('Affilation/<navs>/',navs.affilation_nav, name="affilation_nav"),
    path('IQAC/<navs>/',navs.iqac_nav, name="iqac_nav"),
    path('governing/<navs>/',navs.gov_nav,name='gov_nav'),
    path('admistrative/<navs>/',navs.adm_nav,name='adm_nav'),
    path('teachers-council/<navs>/',navs.tc_nav,name='tc_nav'),
    path('officestaff/<navs>/',navs.ofst_nav,name='offst_nav'),

    #academic nav
    path('rules/<navs>/',navs.rules_navs,name="rules_navs"),
    path('academic/<navs>/',navs.academic_navs,name="aca_avs"),
    path('calandar/<navs>/',navs.cal_navs,name="cal_navs"),
    path('depeartments/<navs>/',navs.dep_navs,name="dep_navs"),

    #admission nav
    path('feestructure/<navs>/',navs.fees_navs),
    path('admission/<navs>/',navs.admission_navs),
    path('carrer-oriented-course/<navs>/',navs.carrer_navs),
    path('exam-structure/<navs>/',navs.exam_navs),

    #library navs
    path('about/<navs>/',navs.library_navs,name="about_lib_nav"),
    path('resources/<navs>/',navs.res_navs,name="res"),
    path('services/<navs>/',navs.serv_navs,name="ser_navs"),
    path('management/<navs>/',navs.management_navs,name="managememnt_navs"),
    path('rules_/<navs>/',navs.rules_navs,name=""),
    path('library/<navs>/',navs.library_navs)


    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
