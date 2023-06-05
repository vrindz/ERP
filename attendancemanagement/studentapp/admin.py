from django.contrib import admin
from .forms import StudentDOB
from .models import Students
from django.core.exceptions import MultipleObjectsReturned
from django.utils.html import format_html


# Register your models here.
class StudentAdminSite(admin.ModelAdmin,StudentDOB):
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
admin.site.register(Students,StudentAdminSite)    
