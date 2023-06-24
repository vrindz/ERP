from django.contrib import admin
from .forms import StudentDOB
from .models import Students,CourseFees,FeeDetails,FeesReceipt
from django.core.exceptions import MultipleObjectsReturned
from django.utils.html import format_html
from django.urls import NoReverseMatch
from .models import *



# Register your models here.
class StudentAdminSite(admin.ModelAdmin,StudentDOB):
    list_display = ("Student","phone","Enquiry_Source","Course","fees_link")
    #list_filter = ("nextdate")

     
    
    readonly_fields = ("verifyphone",)
    
    fieldsets =(("General",{"fields":["Enquiry_Source"]}),
                ("Phone Verification",{"fields":["phone","verifyphone"]}),
                ("Personal Information", {
              "fields": [
                ("Student","Gender"),
                ("Email","Alternative_email"),
                ("Address","Alternative_Address"),
                ("Dob", "Mobile"),
                ("Street","City"),
                ("State","District",),
                ("Pincode","Whatsapp")
            ],
        }),
                 ("Academic Info", {"fields":
                                    [
                                        ("Collegename","year"),
                                        ("Qualification"),
                                        ("Rollno","Register"),
                                     ]}),
                 
                 ("Course Info", {"fields":
                                    [
                                        ("Course"),
                                        ]}),
                ("Photo", {"fields":
                                    [
                                        ("photo"),
                                        
                                     ]}),
                
                ("Student Call Status", {"fields":
                                    [
                                    "Studentcallstatus","nextdate","tostaff","Comments"
                  ]}),)
                
    def fees_link(self, obj):
        try:
            url = f"/admin/studentapp/feedetails/?Students"
            link = f'<a href="{url}">Go</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    fees_link.short_description = 'Fees'
           
    def save_model(self, request, obj, form, change):
        from django.core.exceptions import ObjectDoesNotExist
        if change == False:
            # global res
            try:
                phoneno = obj.phone
                # result = list(Course.objects.filter(id=int(id)).UserTrainers_set.values())
                result = Students.objects.get(phone=phoneno)
            except ObjectDoesNotExist:
                # res = {"message": "Phone does not exist. Proceed"}
                # self.message_user(request, "Candidate has been registered")
                super().save_model(request, obj, form, change)
            except MultipleObjectsReturned:
                self.message_user(request, "Student with phone exists. Please add another.")
            except:
                self.message_user(request, "Something went wrong")
            else:
                self.message_user(request, "Student with phone exists. Please add another.")
        else:
            super().save_model(request, obj, form, change)

    def verifyphone(self, obj):
        return format_html('<a href="#" onclick="verifyPhoneNumber()">Verify Phone Number</a>')


    verifyphone.allow_tags = True
    verifyphone.short_description = ""

    change_form_template = "studentenquiryform.html"
    
    form = StudentDOB


   
    search_fields = ("Student","phone")
      
class CourseFeesAdmin(admin.ModelAdmin):
    list_display = ("course", "fees_type", "amount",)

    fieldsets = (
        ('Fees Details', {
            'fields': ('course', 'fees_type', 'amount','installment_period')
        }),
    )

    def display_installment_period(self, obj):
        return f"{obj.installment_period} months"

    display_installment_period.short_description = 'Installment Period'
class FeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_pay', 'first_pay_amount','payment','second_pay','second_pay_amount','payment','third_pay','third_pay_amount','payment')
    list_filter = ('student',)

    def payment(self, obj):
        url = reverse('admin:studentapp_feesreceipt_add')  # Replace 'yourapp' with the actual name of your app
        link = f'<a href="{url}?student_id={obj.student_id}">Pay</a>'
        return format_html(link)

    payment.short_description = 'Payment'

class FeesReceiptAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'paid_amount', 'receipt_number', 'payment_mode', 'description', 'collected_to_account')

             
admin.site.register(Students,StudentAdminSite)
admin.site.register(CourseFees,CourseFeesAdmin)
admin.site.register(FeeDetails,FeeDetailsAdmin)
admin.site.register(FeesReceipt,FeesReceiptAdmin)
     

   
