from django.db import models
from uuid import uuid4
# Create your models here.

class StudentSignup(models.Model):
    
    Rollno = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000000)

class StudentData(models.Model):
    
    year = models.CharField(max_length=1000)
    rollno = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    semester = models.CharField(max_length=1000)
    branch = models.CharField(max_length=1000)
    semester_marksheet = models.FileField()
    semester_registration = models.FileField()
    semester_routine = models.FileField()
    semester_admit = models.FileField()
    course_type = models.CharField(max_length=1000)

    
class Marksheets(models.Model):
    year = models.CharField(max_length=1000)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    marksheet_pdf = models.FileField(upload_to="media/files/marksheets")
    roll        = models.CharField(max_length=1000)
    course_type = models.CharField(max_length=1000)

    


class routine(models.Model):
    year          = models.CharField(max_length=1000)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    day           = models.CharField(max_length=1000)
    time          = models.CharField(max_length=1000)
    subject       = models.CharField(max_length=1000)
    teacher       = models.CharField(max_length=1000)
    course_type = models.CharField(max_length=1000)


class Registration(models.Model):
    year             = models.CharField(max_length=1000)
    semester         = models.CharField(max_length=1000)
    branch           = models.CharField(max_length=1000)
    registration_pdf = models.FileField(upload_to="media/files/registration")
    roll             = models.CharField(max_length=1000)
    course_type = models.CharField(max_length=1000)


class AdmitCard(models.Model):
    year = models.CharField(max_length=1000)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    admit_pdf     = models.FileField(upload_to="media/files/admitcard")
    roll          = models.CharField(max_length=1000)
    course_type = models.CharField(max_length=1000)



class ExamRoutine(models.Model):
    year = models.CharField(max_length=1000)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    exam_pdf     = models.FileField(upload_to="media/files/admitcard")
    course_type = models.CharField(max_length=1000)

class Syllabus(models.Model):
    year = models.CharField(max_length=1000)
    semester      = models.CharField(max_length=1000)
    branch        = models.CharField(max_length=1000)
    syllabus_pdf     = models.FileField(upload_to="media/files/admitcard")
    course_type = models.CharField(max_length=1000)


class IdentityCard(models.Model):
    id = models.BigAutoField(primary_key=True,default=uuid4,editable=False)
    year = models.CharField(max_length=1000)
    rollno = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    semester = models.CharField(max_length=1000)
    branch = models.CharField(max_length=1000)
    course_type = models.CharField(max_length=1000)
    address  = models.CharField(max_length=1000)
    blood_group = models.CharField(max_length=1000)
    registrationNo = models.CharField(max_length=1000)
     
class RegisterRollNo(models.Model):
   
    name = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return str(self.name)
        









    

    

    





    
    


