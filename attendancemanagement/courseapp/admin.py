
from .models import Company,State,District,Branch,Enquirysource,FollowUpStatus,Qualification,Course,Batch,MasterData,Syllabus
# Register your models here.
from django.contrib import admin
from .forms import BatchForm
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
class customeuseradmin(admin.ModelAdmin):
    list_display=['username','email','date_joined']
    ordering=['username']
class customegroupadmin(admin.ModelAdmin):
    list_display=["name"]  
    ordering=['name']
class AttendanceAdminSite(AdminSite):
    def get_app_list(self, request):
        ordering = {
            "Companies": 1,
            "States": 2,
            "Districts": 3,
            "Branches": 4,
            "Enquiry Sources": 5,
            "Follow up statuses": 6,
            "Qualifications": 7,
            "Batch": 8,
            "Syllabus": 9,
            "Courses": 10,
            "Master Data": 11
        }
        appordering={
            "courseapp":1,
            "studentapp":2,
            "Authentication and Authorization":3,
            
        }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = list(app_dict.values())
        # app_list.sort(key=lambda x:appordering[x['name']])

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

            return app_list
mysite= AttendanceAdminSite()
admin.site=mysite
class BatchFormAdmin(admin.ModelAdmin):
     form = BatchForm
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('District_name', 'State_name')
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('Trainers',)


admin.site.register(Company)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Enquirysource)
admin.site.register(FollowUpStatus)
admin.site.register(Qualification)
admin.site.register(Course,CourseAdmin)
admin.site.register(Batch,BatchFormAdmin)
admin.site.register(MasterData)
admin.site.register(Syllabus)
admin.site.register(User)
admin.site.register(Group)


