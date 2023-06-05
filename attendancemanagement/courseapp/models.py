from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.admin import AdminSite
from datetime import datetime,timedelta
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import User





#Create your models here.
class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
#    # isactive = models.BooleanField(default=True, verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #  class Meta:
    #     abstract = True
    #     ordering = ['-isactive']
class Company(models.Model):
    Company = models.CharField(max_length=100)
    Address1 = models.CharField(max_length=100,blank=True)
    Address2 = models.CharField(max_length=100, blank=True)
    Address3 = models.CharField(max_length=100, blank=True)
    Phone = models.CharField(max_length=100)
    Email = models.EmailField(blank=True)
    Website = models.URLField(blank=True)
    Logo = models.ImageField(max_length=255)
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Companies"

class State(models.Model):
    State_name = models.CharField(max_length=100)
    active= models.BooleanField(default=False)

    def __str__(self):
        return self.State_name
    class Meta:
        verbose_name_plural = "States"
class District(models.Model):
    State = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    District_name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.State
    def __str__(self):
        return self.District_name

    class Meta:
        verbose_name_plural = "Districts"
class Branch(models.Model):
    Branch = models.CharField(max_length=255)
    Branch_code = models.CharField(max_length=255)
    Address = models.CharField(max_length=100,blank=True)
    Street = models.CharField(max_length=100,blank=True)
    State = models.ForeignKey(State,on_delete=models.CASCADE,blank=False)
    District = ChainedForeignKey(
        District,
        chained_field="State",
        chained_model_field="State_name",
        show_all=False,
        auto_choose=True,
        sort=True)
    Pincode = models.CharField(max_length=50,blank=True)
    Mobile = models.CharField(max_length=255)
    Email = models.EmailField(blank=True)
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Branches"



class Enquirysource(models.Model):
    Enquirysourcename = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Enquiry Sources"

class FollowUpStatus(models.Model):
    followupstatusname = models.CharField(max_length=255,unique=True)
    BOOL_CHOICES = ((True,'Yes'),(False,'No'))
    followupstatus= models.BooleanField(choices=BOOL_CHOICES)
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Follow up statuses"

    def __str__(self):
        return self.followupstatusname



class Qualification(models.Model):
    Qualificationname = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Qualificationname
    class Meta:
        verbose_name_plural = "Qualifications"
# class Course(models.Model):
#     Course = models.CharField(max_length=255)
#     active = models.BooleanField(default=False)
#     class Meta:
#         verbose_name_plural = "Course"

#     def __str__(self):
#         return self.Course

class Batch(models.Model):
    batch = models.CharField(max_length=150,unique=True,null=True)
    # Course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course",
    #                            null=True, blank=False, limit_choices_to={"isactive": True})
    Trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Trainer", null=True, blank=False, related_name="Trainer", limit_choices_to={"is_active": True, "groups__name": 'Faculty'})
    
    
    start_date = models.DateTimeField()
    end_date = models.DateField()
    closed = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.Trainer
    def __str__(self):
        return self.Course
    
    
    class Meta:
        verbose_name_plural = "Batch"
class Syllabus(models.Model):
    Syllabus_name = models.CharField(max_length=255)
    def __str__(self):
        return self.Syllabus_name
    class Meta:
        verbose_name_plural ="Syllabus"

class MasterData(models.Model):
    Name = models.CharField(max_length=255)
    Value = models.CharField(max_length=255)
    Type = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Master Data"
class Course(models.Model):
    Course = models.CharField(max_length=200, unique=True)
    Coursecode = models.CharField(max_length=200, unique=True, null=True)
    Trainers = models.ManyToManyField(User, related_name="UserTrainers", blank=True, limit_choices_to={"is_active": True, "groups__name": 'Faculty'})
    active = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Courses"
    def __str__(self):
        return self.Course   
    

    