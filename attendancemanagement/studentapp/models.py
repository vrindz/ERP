from urllib.parse import urlencode
from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.core.validators import RegexValidator
from courseapp.models import State,District,Qualification,Course
import datetime
from django.contrib.auth.models import User
from django.urls import reverse


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
    City = models.CharField(max_length=50,null=True,verbose_name="City",blank=True)
    Pincode = models.CharField(max_length=10,null=True,verbose_name="Pincode",blank=True)
    Whatsapp = models.CharField(max_length=10,null=True,verbose_name="Whatsapp")

    

    Collegename = models.CharField(max_length=100,null=True,verbose_name="College Name")
    YEAR_CHOICES = []
    for r in range((datetime.datetime.now().year - 15), (datetime.datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))
    year = models.PositiveIntegerField(choices=YEAR_CHOICES, blank=False, null=True, verbose_name="Year of Pass")
    Qualification = models.ForeignKey(Qualification,on_delete=models.CASCADE,verbose_name="Qualification",null=True)
    Rollno = models.CharField(max_length=10,null=True,verbose_name="Roll No")
    Register = models.CharField(max_length=10,null=True,verbose_name="Registration No")
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Course",null=True)
    photo = models.ImageField(verbose_name="Photo",null=True)
    BOOL_CHOICES = ((True,'Yes'),(False,'No'))
    Studentcallstatus = models.BooleanField(choices=BOOL_CHOICES,verbose_name="Student Call Status",null=True)
    nextdate = models.DateField(verbose_name="Next Follow-up Date",null=True)
    tostaff = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="To Staff",null=True)
    Comments = models.CharField(max_length=10,null=True,verbose_name="Comments")
    
    
    def __str__(self):
        return self.Student

    class Meta:
        verbose_name_plural = "Students"

class CourseFees(models.Model):
    course = models.ForeignKey(Course,null=True, on_delete=models.CASCADE)
    fees_type = models.CharField(max_length=12,null=True, choices=(('one_time', 'One Time'), ('two_time', 'Two Time'), ('three_time', 'Three Time'),('registration','Registration')))
    amount = models.IntegerField(null=True)
    #tax = models.DecimalField(max_digits=3,decimal_places=1,null=True,blank=True)
    installment_period = models.IntegerField(null=True)

    def __str__(self):
        return self.fees_type
    
    class Meta:
        verbose_name_plural = "CourseFees"


gender_choice = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER'),

)
yes_choice= (
    ('yes','Yes'),
    ('no','No'),
)
CHOICES = (
    ('one_times', 'One Time'),
    ('two_times', 'Two Times'),
    ('three_times', 'Three Times')
)


class FeeDetails(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    selection_type = models.CharField(null=True,max_length=20, choices=CHOICES)
    first_pay = models.DateField(null=True, blank=True)
    first_pay_amount = models.IntegerField(null=True, blank=True)
    second_pay = models.DateField(null=True, blank=True)
    second_pay_amount = models.IntegerField(null=True, blank=True)
    third_pay = models.DateField(null=True, blank=True)
    third_pay_amount = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.selection_type == 'one_times':
            self.second_pay = None
            self.second_pay_amount = None
            self.third_pay = None
            self.third_pay_amount = None
        elif self.selection_type == 'two_times':
            self.third_pay = None
            self.third_pay_amount = None

        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Fees Details"
    def __str__(self):
        return self.FeeDetails
class FeesReceipt(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cheque', 'Cheque'),
    ]

    COLLECTED_TO_ACCOUNT_CHOICES = [
        ('oneteam ac 1', 'Oneteam ac 1'),
        ('oneteam ac 2', 'Oneteam ac 2'),
        ('oneteam ac 3', 'Oneteam ac 3'),
    ]
    student = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=50)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_to_account = models.CharField(max_length=100, choices=COLLECTED_TO_ACCOUNT_CHOICES)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    description = models.TextField()
    receipt_image = models.ImageField(upload_to='receipts/')
    class Meta:
        verbose_name_plural = "Fees Receipt"
    