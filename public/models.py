from django.db import models

# Create your models here.

class SliderImage(models.Model):
    img1 = models.ImageField(upload_to="media/pics/slider",null=True,blank=True)
    event = models.CharField(max_length=30,null=True,blank=True)

class PrincipleImage(models.Model):
    principle_name = models.CharField(max_length=30,null=True,blank=True)
    img1 = models.ImageField(upload_to="media/pics/principle",null=True,blank=True)

class PhotoGallary(models.Model):
    img1 = models.ImageField(upload_to="media/pics/gallary",null=True,blank=True)
    
class TeachersCouncil(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    qualification = models.CharField(max_length=50,null=True,blank=True)
    desgination   = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Courses(models.Model):
    coursename = models.CharField(max_length=100,null=True,blank=True)
    courseseats = models.CharField(max_length=30,null=True,blank=True)
    year        = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.coursename)

class OfficeStaff(models.Model):
    name = models.CharField(max_length=30,null=True)
    desgination   = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return str(self.name)

class AdministrativeOfficer(models.Model):
    name = models.CharField(max_length=30,null=True)
    desgination   = models.CharField(max_length=50,null=True)
    image         = models.ImageField(upload_to="media/pics/administrative",null=True)

    def __str__(self) -> str:
        return str(self.name)

class GoverningBody(models.Model):
    name = models.CharField(max_length=30,null=True)
    desgination   = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return str(self.name)

class librarian(models.Model):
    name = models.CharField(max_length=100,null=True)
    desgination   = models.CharField(max_length=100,null=True)
    image         = models.ImageField(upload_to="media/pics/lib",null=True)
    mail_id       = models.EmailField()
    whatsapp      = models.CharField(max_length=10,null=True)

    def __str__(self) -> str:
        return str(self.name)

class AdmissionNotice(models.Model):
    hounours_course_date = models.CharField(max_length=100,null=True)
    program_course_date = models.CharField(max_length=100,null=True)
    merit_publish_date = models.CharField(max_length=100,null=True)
    carrer_counceling_date = models.CharField(max_length=100,null=True)
    fees_payment = models.CharField(max_length=100,null=True)
    document_verification = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=1000,null=True)

class course_fee(models.Model):
    course_name = models.CharField(max_length=100,null=True)
    course_fee = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return str(self.course_name)


class FacultyMembers(models.Model):
    name = models.CharField(max_length=30,null=True)
    desgination   = models.CharField(max_length=50,null=True,blank=True)
    img      = models.ImageField(upload_to="media/pics/faculty",null=True,blank=True)
    department    = models.CharField(max_length=100,null=True,blank=True)
    specialization = models.CharField(max_length=100,null=True,blank=True)
    qualification  = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class PublicQueryForm(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email  = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    query      = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.first_name)

    
class Resource(models.Model):
    online_public_access_catalog    = models.CharField(max_length=1000,null=True,blank=True)
    dbm_whatsapp_group_link1        = models.CharField(max_length=1000,null=True,blank=True)
    dbm_whatsapp_group_link2        = models.CharField(max_length=1000,null=True,blank=True)
    dbm_lib_whatsapp_group_link3    = models.CharField(max_length=1000,null=True,blank=True)
    wbclolr                         = models.CharField(max_length=1000,null=True,blank=True)
    ndli                            = models.CharField(max_length=1000,null=True,blank=True)
    internet_archive                = models.CharField(max_length=1000,null=True,blank=True)
    

    def __str__(self) -> str:
        return "LINKS"
class Book(models.Model):
    department_name = models.CharField(max_length=1000,null=True,blank=True)
    books_in_digit  = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.department_name)

class ReferenceBooks(models.Model):
    Reference_catagory = models.CharField(max_length=1000,null=True,blank=True)
    books_available    = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.Reference_catagory)

class MamangementMembers(models.Model):
    slno = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Canteen(models.Model):
    image = models.ImageField(upload_to="media/pics/canteen",null=True,blank=True)

    def __str__(self) -> str:
        return "canteen image"


class CarrerGuidence(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    link = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class AcademicCalander(models.Model):
    description = models.CharField(max_length=100,null=True,blank=True)
    link = models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.description)
class ComputerCenter(models.Model):
    image = models.ImageField(upload_to="media/pics/computerlab",null=True,blank=True)
    def __str__(self) -> str:
        return "computerlab"


class IndexAlert(models.Model):
    message = models.CharField(max_length=1000000)
    def __str__(self) -> str:
        return "index marquee msg"


class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_details = models.CharField(max_length=200)
    notice_link_name = models.CharField(max_length=200,null=True,blank=True)
    notice_file = models.FileField(upload_to="media/notice/files",null=True,blank=True)

class feedback(models.Model):
    name = models.CharField(max_length=200)
    msg = models.CharField(max_length=200)

class newsletter(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)
    
class notice_files(models.Model):
    label = models.CharField(max_length=100)
    file  = models.FileField()

class DocumentRequired(models.Model):
    label = models.CharField(max_length=1000)


class AdmissionQuery(models.Model):
    pass








    



    





    
    


    
    





    
    