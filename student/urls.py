from django.contrib import admin
from django.urls import path,include
from student.views import *
from django.conf import settings
from django.conf.urls.static import static
d = Dashboard()
s = Signup()
l = Login()
g = geo_locate()
urlpatterns= [
    
    path("dashboard/",d.show_dashboard,name="dashboard"),
   
    
    path("signup/",s.show_signup,name="signup"),
    path("signup/login/",s.redirect_login,name=""),
    path("signup/createnew/",s.createuser),
    path("login/",l.show_login,name="login"),
    path("dashboard/home/",home,name=""),
    path("dashboard/logout/",logout,name=""),
   
    path("login/verify/",l.verify_login,name=""),
    path("login/signup/",s.redirect_signup,name="")
    
]