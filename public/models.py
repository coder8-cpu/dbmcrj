from django.db import models

# Create your models here.

class SliderImage(models.Model):
    img1 = models.ImageField(upload_to="media/pics/slider")
    img2 = models.ImageField(upload_to="media/pics/slider")
    img3 = models.ImageField(upload_to="media/pics/slider")
    img4 = models.ImageField(upload_to="media/pics/slider")
    img5 = models.ImageField(upload_to="media/pics/slider")

class PrincipleImage(models.Model):
    principle_name = models.CharField(max_length=30)
    img1 = models.ImageField(upload_to="media/pics/principle")

class PhotoGallary(models.Model):
    img1 = models.ImageField(upload_to="media/pics/gallary")
    img2 = models.ImageField(upload_to="media/pics/gallary")
    img3 = models.ImageField(upload_to="media/pics/gallary")
    img4 = models.ImageField(upload_to="media/pics/gallary")
    img5 = models.ImageField(upload_to="media/pics/gallary")
    img6 = models.ImageField(upload_to="media/pics/gallary")
    img7 = models.ImageField(upload_to="media/pics/gallary")
    img8 = models.ImageField(upload_to="media/pics/gallary")

class TeachersCouncil(models.Model):
    name = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50)
    desgination   = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

class Courses(models.Model):
    coursename = models.CharField(max_length=100)
    courseseats = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.coursename)

class OfficeStaff(models.Model):
    name = models.CharField(max_length=30)
    desgination   = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

class AdministrativeOfficer(models.Model):
    name = models.CharField(max_length=30)
    desgination   = models.CharField(max_length=50)
    image         = models.ImageField(upload_to="media/pics/administrative")

    def __str__(self) -> str:
        return str(self.name)

class GoverningBody(models.Model):
    name = models.CharField(max_length=30)
    desgination   = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)

class librarian(models.Model):
    name = models.CharField(max_length=100,)
    desgination   = models.CharField(max_length=100)
    image         = models.ImageField(upload_to="media/pics/lib")
    mail_id       = models.EmailField()
    whatsapp      = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.name)

class AdmissionNotice(models.Model):
    hounours_course_date = models.CharField(max_length=100)
    program_course_date = models.CharField(max_length=100)
    merit_publish_date = models.CharField(max_length=100)
    carrer_counceling_date = models.CharField(max_length=100)
    fees_payment = models.CharField(max_length=100)
    document_verification = models.CharField(max_length=100)
    year = models.CharField(max_length=1000)

class course_fee(models.Model):
    course_name = models.CharField(max_length=100)
    course_fee = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.course_name)


class FacultyMembers(models.Model):
    name = models.CharField(max_length=30)
    desgination   = models.CharField(max_length=50)
    img      = models.ImageField(upload_to="media/pics/faculty")
    department    = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    qualification  = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

class PublicQueryForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    query      = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.first_name)

    


    



    





    
    


    
    





    
    