from django.contrib import admin
from django.urls import path,include
from student.views import *
from django.conf import settings
from django.conf.urls.static import static
d = Dashboard()
s = Signup()
l = Login()
urlpatterns= [
    path("dashboard/",d.show_dashboard),
    path("dashboard/<navs>/",d.dashboard_navs),
    path("marksheet/",d.show_marksheet,name="marksheet"),
    path("marksheet/<navs>/",d.dashboard_navs,name=""),
    path("admitcard/",d.show_admit,name="admitcard"),
    path("admitcard/<navs>/",d.dashboard_navs,name=""),
    path("notification/",d.show_notification,name="notification"),
    path("notification/<navs>/",d.dashboard_navs,name=""),
    path("syllabus/",d.show_sylabus,name="syllabus"),
    path("syllabus/<navs>/",d.dashboard_navs,name=""),
    path("registration/",d.show_registration,name="reg"),
    path("registration/<navs>/",d.dashboard_navs,name=""),
    path("routine/",d.show_routine,name="routine"),
    path("routine/<navs>/",d.dashboard_navs,name=""),
    path("examdschedule/",d.show_exams,name="exam_schedule"),
    path("examdschedule/<navs>/",d.dashboard_navs,name=""),
    
    path("signup/",s.show_signup,name="signup"),
    path("signup/createnew/",s.createuser),
    path("login/",l.show_login,name="login"),
    path("logout/",d.logout,name="logout"),
    path("login/verify/",l.verify_login,name="login")
]