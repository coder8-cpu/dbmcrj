from django.db import models

# Create your models here.

class SliderImage(models.Model):
    img1           = models.ImageField(upload_to="media/pics/slider",null=True,blank=True)
    event          = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.event)
class IndexSliderImage(models.Model):
    img1           = models.ImageField(upload_to="media/pics/slider",null=True,blank=True)
    name           = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)
class Manage_rep(models.Model):
    name          = models.CharField(max_length=30,null=True)
    desgination     = models.CharField(max_length=50,null=True)
class Ext_rep(models.Model):
    name              = models.CharField(max_length=3000,null=True)
    desgination         = models.CharField(max_length=5000,null=True)
class Facul_rep(models.Model):
    name                  = models.CharField(max_length=30000,null=True)
    desgination             = models.CharField(max_length=50009,null=True)
class PrincipleImage(models.Model):
    principle_name            = models.CharField(max_length=30,null=True,blank=True)
    img1                        = models.ImageField(upload_to="media/pics/principle",null=True,blank=True)

    def __str__(self) -> str:
        return str(self.principle_name)


class PhotoGallary(models.Model):
    img1           = models.ImageField(upload_to="media/pics/gallary",null=True,blank=True)

    def __str__(self) -> str:
        return "Photos"

    
class TeachersCouncil(models.Model):
    name           = models.CharField(max_length=30,null=True,blank=True)
    qualification    = models.CharField(max_length=50,null=True,blank=True)
    desgination        = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Courses(models.Model):
    coursename           = models.CharField(max_length=100,null=True,blank=True)
    courseseats            = models.CharField(max_length=30,null=True,blank=True)
    year                     = models.CharField(max_length=10,null=True,blank=True)
    course_main_subject_name   = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.coursename)

class CoursesFee(models.Model):
    coursename   = models.CharField(max_length=100,null=True,blank=True)
    coursefee   = models.CharField(max_length=30,null=True,blank=True)
    year       = models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.coursename)

class OfficeStaff(models.Model):
    name        = models.CharField(max_length=30,null=True,blank=True)
    desgination   = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class AdministrativeOfficer(models.Model):
    name            = models.CharField(max_length=30,null=True,blank=True)
    desgination       = models.CharField(max_length=50,null=True,blank=True)
    image               = models.ImageField(upload_to="media/pics/administrative",null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)
class IQAC(models.Model):
    name            = models.CharField(max_length=30,null=True,blank=True)
    desgination       = models.CharField(max_length=50,null=True,blank=True)
    image               = models.ImageField(upload_to="media/pics/administrative",null=True,blank=True)

class AQAR(models.Model):
    label    = models.CharField(max_length=1000,null=True,blank=True)
    file       = models.FileField(upload_to="media/aqar/pdf",null=True,blank=True)

class Departments(models.Model):
    name = models.CharField(max_length=100,blank=True)
    image  = models.ImageField(upload_to="media/departments/img",blank=True)
    about    = models.CharField(max_length=100000000,null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.name)
class Eresources(models.Model):
    departments              = models.ForeignKey(Departments,on_delete=models.CASCADE)
    Resource_link            = models.CharField(max_length=300,null=True,blank=True,default="/")
    Resource_link_file       = models.FileField(upload_to="media/departments/resource/file/",null=True,blank=True) 
    honours_resources_label  = models.CharField(max_length=300,null=True,blank=True)
    honours_resources        = models.FileField(upload_to="media/departments/honours",null=True,blank=True)
    program_resources_label  = models.CharField(max_length=300,null=True)
    program_resources        = models.FileField(upload_to="media/deparments/program",null=True,blank=True)
    def __str__(self) -> str:
        return str(self.departments.name)

class DepartmentsFaculty(models.Model):
    name           = models.CharField(max_length=30,null=True,blank=True)
    desgination    = models.CharField(max_length=50,null=True,blank=True)
    img            = models.ImageField(upload_to="media/pics/faculty",null=True,blank=True)
    department     = models.ForeignKey(Departments,on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100,null=True,blank=True)
    qualification  = models.CharField(max_length=100,null=True,blank=True)
    cv             = models.FileField(upload_to="media/deparments/cv",null=True,blank=True)

    def __str__(self) -> str:
        return str(self.department.name)

class GoverningBody(models.Model):
    name          = models.CharField(max_length=30,null=True,blank=True)
    desgination   = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class librarian(models.Model):
    name          = models.CharField(max_length=100,null=True,blank=True)
    desgination   = models.CharField(max_length=100,null=True,blank=True)
    image         = models.ImageField(upload_to="media/pics/lib",null=True,blank=True)
    mail_id       = models.EmailField()
    whatsapp      = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class AdmissionNotice(models.Model):
    hounours_course_date     = models.CharField(max_length=100,null=True,blank=True)
    program_course_date      = models.CharField(max_length=100,null=True,blank=True)
    merit_publish_date       = models.CharField(max_length=100,null=True,blank=True)
    carrer_counceling_date   = models.CharField(max_length=100,null=True,blank=True)
    fees_payment             = models.CharField(max_length=100,null=True,blank=True)
    document_verification    = models.CharField(max_length=100,null=True,blank=True)
    year                     = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.year)


class course_fee(models.Model):
    course_name   = models.CharField(max_length=100,null=True,blank=True)
    course_fee    = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.course_name)


class FacultyMembers(models.Model):
    name           = models.CharField(max_length=30,null=True,blank=True)
    desgination    = models.CharField(max_length=50,null=True,blank=True)
    img            = models.ImageField(upload_to="media/pics/faculty",null=True,blank=True)
    department     = models.CharField(max_length=100,null=True,blank=True)
    specialization = models.CharField(max_length=100,null=True,blank=True)
    qualification  = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class PublicQueryForm(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email  = models.CharField(max_length=100,null=True,blank=True)
    subject  = models.CharField(max_length=100,null=True,blank=True)
    query      = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

    
class Resource(models.Model):
    label    = models.CharField(max_length=1000,null=True,blank=True)
    link       = models.CharField(max_length=1000,null=True,blank=True)
    file         = models.FileField()
    year           = models.CharField(max_length=1000,null=True,blank=True)

   

    def __str__(self) -> str:
        return str(self.label)
class currentyear(models.Model):
    year     = models.CharField(max_length=1000,null=True,blank=True)

   

    def __str__(self) -> str:
        return str(self.year)

class Book(models.Model):
    department_name = models.CharField(max_length=1000,null=True,blank=True)
    books_in_digit    = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.department_name)

class ReferenceBooks(models.Model):
    Reference_catagory = models.CharField(max_length=1000,null=True,blank=True)
    books_available      = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.Reference_catagory)

class MamangementMembers(models.Model):
    slno = models.CharField(max_length=1000,null=True,blank=True)
    name   = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Canteen(models.Model):
    image = models.ImageField(upload_to="media/pics/canteen",null=True,blank=True)

    def __str__(self) -> str:
        return "canteen image"


class CarrerGuidence(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    link   = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class AcademicCalander(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    file   = models.FileField(upload_to="media/academic-calender/",null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)
class ComputerCenter(models.Model):
    image       = models.ImageField(upload_to="media/pics/computerlab",null=True,blank=True)
    def __str__(self) -> str:
        return "computerlab"


class IndexAlert(models.Model):

    message = models.CharField(max_length=1000000,blank=True,null=True)
    link = models.CharField(max_length=1000000,null=True,blank=True)
    file = models.FileField(max_length=1000000,null=True,blank=True)
    def __str__(self) -> str:
        return "index marquee msg"


class Notice(models.Model):
    notice_title = models.CharField(max_length=200,blank=True,null=True)
    notice_details = models.CharField(max_length=200,blank=True,null=True)
    notice_link_name = models.CharField(max_length=200,null=True,blank=True)
    notice_file        = models.FileField(upload_to="media/notice/files",null=True,blank=True)

class feedback(models.Model):
    name  = models.CharField(max_length=200,blank=True,null=True)
    msg   = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.name)


class newsletter(models.Model):
    name  = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self) -> str:
        return str(self.name)
    
class notice_files(models.Model):
    label = models.CharField(max_length=100,blank=True,null=True)
    file  = models.FileField()

    def __str__(self) -> str:
        return str(self.label)

class DocumentRequired(models.Model):
    label = models.CharField(max_length=1000,blank=True,null=True)
    
    def __str__(self) -> str:
        return str(self.label)













    



    





    
    


    
    





    
    