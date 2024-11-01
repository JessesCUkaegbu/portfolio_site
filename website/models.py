from django.db import models

# Create your models here.
class AboutMe(models.Model):
    skill_1 = models.CharField(max_length=20)
    skill_2 = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)
    
class Service(models.Model):
    title = models.CharField(max_length=20)
    info = models.TextField(blank=True, null=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="Testimony")
    testimony = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=20)

class Clients(models.Model):
    company_logo = models.ImageField(upload_to="Client")

class Price(models.Model):
   service = models.CharField(max_length=30)
   price = models.IntegerField()
   hour = models.IntegerField()
   offer_note = models.TextField()

class Education(models.Model):
   year = models.IntegerField()
   university = models.CharField(max_length=30)
   degree_status = models.CharField(max_length=30)
   info = models.TextField()

class Experience(models.Model):
   number_of_year = models.IntegerField()
   company_name = models.CharField(max_length=30)
   role = models.CharField(max_length=30)
   contribution = models.TextField()

class Certificate(models.Model):
   title = models.CharField(max_length=30)
   img =  models.ImageField(upload_to="Certificate")
   date = models.IntegerField()
   entity = models.CharField(max_length=30)

class DesignSkill(models.Model):
   name = models.CharField(max_length=30)
   strength_level = models.IntegerField()

class CodingSkill(models.Model):
   name = models.CharField(max_length=30)
   strength_level = models.IntegerField()

class Blog(models.Model):
   title = models.CharField(max_length=30)
   img =  models.ImageField(upload_to="Certificate")
   pub_date = models.IntegerField()
   post = models.CharField(max_length=10)

class ContactForm(models.Model):
   full_name = models.CharField(max_length=30)
   email =  models.EmailField()
   subject = models.CharField(max_length=100)
   message = models.TextField()

class Portfolio(models.Model):
   project_name = models.CharField(max_length=30)
   img = models.ImageField(upload_to="portfolio")
   video = models.FileField()
   detail = models.TextField()