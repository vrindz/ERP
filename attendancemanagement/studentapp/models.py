from urllib.parse import urlencode
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.core.validators import RegexValidator
from courseapp.models import State,District,Qualification,Course
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    EnquirySource = (
        ("facebook","facebook"),
        ("indeed","indeed"),
        ("youtube","youtube"),
        ("instagram","instagram")
    )
    Enquiry_Source=models.CharField(max_length=20,choices=EnquirySource,verbose_name="Enquiry Source")
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17,verbose_name="Phone",null=True)  # Validators should be a list
    Student = models.CharField(max_length=10,null=True,verbose_name="Student")
    Gender = models.CharField(max_length=10,null=True,verbose_name="Gender")
    Email = models.EmailField(verbose_name="Email")
    Alternative_email = models.CharField(max_length=10,null=True,verbose_name="Alternative Email",blank=True)
    Address = models.CharField(max_length=20,null=True,verbose_name="Address",blank=True)
    Alternative_Address=models.CharField(max_length=20,null=True,verbose_name="Alternative Address",blank=True)
    Dob = models.DateField(verbose_name="Dob",null=True,max_length=10)
    Mobile = models.CharField(max_length=12,null=True, verbose_name="Mobile", blank=True)

    Street = models.CharField(max_length=10,null=True,verbose_name="Street",blank=True)
    State = models.ForeignKey(State,on_delete=models.CASCADE,blank=False,null=True)
    District = ChainedForeignKey(
        District,
        chained_field="State",
        chained_model_field="State_name",
        show_all=False,
        null=True,
        auto_choose=True,
        sort=True)
    City = models.CharField(max_length=10,null=True,verbose_name="City",blank=True)
    Pincode = models.CharField(max_length=10,null=True,verbose_name="Pincode",blank=True)
    Whatsapp = models.CharField(max_length=10,null=True,verbose_name="Whatsapp")

    

    Collegename = models.CharField(max_length=10,null=True,verbose_name="College Name")
    YEAR_CHOICES = []
    for r in range((datetime.datetime.now().year - 15), (datetime.datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))
    year = models.PositiveIntegerField(choices=YEAR_CHOICES, blank=False, null=True, verbose_name="Year of Pass")
    Qualification = models.ForeignKey(Qualification,on_delete=models.CASCADE,verbose_name="Qualification",null=True)
    #Qualification = models.CharField(max_length=10,null=True,verbose_name="Qualification")
    Rollno = models.CharField(max_length=10,null=True,verbose_name="Roll No")
    Register = models.CharField(max_length=10,null=True,verbose_name="Registration No")
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Course",null=True)
    photo = models.ImageField(verbose_name="Photo",null=True)
    BOOL_CHOICES = ((True,'Yes'),(False,'No'))
    Studentcallstatus = models.BooleanField(choices=BOOL_CHOICES,verbose_name="Student Call Status",null=True)
    nextdate = models.DateField(verbose_name="Next Follow-up Date",null=True)
    tostaff = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="To Staff",null=True)
    #tostaff = models.CharField(max_length=10,null=True,verbose_name="To Staff")
    Comments = models.CharField(max_length=10,null=True,verbose_name="Comments")
    

    class Meta:
        verbose_name_plural = "Students"