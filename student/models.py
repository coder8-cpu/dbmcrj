from django.db import models
from uuid import uuid4
# Create your models here.

class StudentSignup(models.Model):
    
    Rollno = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)
    password = models.CharField(max_length=1000000,null=True,blank=True)




class StudentData(models.Model):
    
    year = models.CharField(max_length=1000,null=True,blank=True)
    rollno = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)
    semester = models.CharField(max_length=1000,null=True,blank=True)
    branch = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)

    
class Marksheets(models.Model):
    year = models.CharField(max_length=1000,null=True,blank=True)
    semester      = models.CharField(max_length=1000,null=True,blank=True)
    branch        = models.CharField(max_length=1000,null=True,blank=True)
    marksheet_pdf = models.FileField(upload_to="media/files/marksheets",null=True,blank=True)
    roll        = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)

    


class routine(models.Model):
    year          = models.CharField(max_length=1000,null=True,blank=True)
    semester      = models.CharField(max_length=1000,null=True,blank=True)
    branch        = models.CharField(max_length=1000,null=True,blank=True)
    day           = models.CharField(max_length=1000,null=True,blank=True)
    time          = models.CharField(max_length=1000,null=True,blank=True)
    subject       = models.CharField(max_length=1000,null=True,blank=True)
    teacher       = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000)


class Registration(models.Model):
    year             = models.CharField(max_length=1000,null=True,blank=True)
    semester         = models.CharField(max_length=1000,null=True,blank=True)
    branch           = models.CharField(max_length=1000,null=True,blank=True)
    registration_pdf = models.FileField(upload_to="media/files/registration",null=True,blank=True)
    roll             = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)


class AdmitCard(models.Model):
    year = models.CharField(max_length=1000,null=True,blank=True)
    semester      = models.CharField(max_length=1000,null=True,blank=True)
    branch        = models.CharField(max_length=1000,null=True,blank=True)
    admit_pdf     = models.FileField(upload_to="media/files/admitcard",null=True,blank=True)
    roll          = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)



class ExamRoutine(models.Model):
    year = models.CharField(max_length=1000,null=True,blank=True)
    semester      = models.CharField(max_length=1000,null=True,blank=True)
    branch        = models.CharField(max_length=1000,null=True,blank=True)
    exam_pdf     = models.FileField(upload_to="media/files/admitcard",null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)

class Syllabus(models.Model):
    year = models.CharField(max_length=1000,null=True,blank=True)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    syllabus_pdf     = models.FileField(upload_to="media/files/admitcard")
    course_type = models.CharField(max_length=1000)


class IdentityCard(models.Model):
    id = models.BigAutoField(primary_key=True,default=uuid4,editable=False)
    year = models.CharField(max_length=1000,null=True,blank=True)
    rollno = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)
    semester = models.CharField(max_length=1000,null=True,blank=True)
    branch = models.CharField(max_length=1000,null=True,blank=True)
    course_type = models.CharField(max_length=1000,null=True,blank=True)
    address  = models.CharField(max_length=1000,null=True,blank=True)
    blood_group = models.CharField(max_length=1000,null=True,blank=True)
    registrationNo = models.CharField(max_length=1000,null=True,blank=True)
     
class RegisterRollNo(models.Model):
   
    name = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class studentfriends(models.Model):
    pass

        









    

    

    





    
    


