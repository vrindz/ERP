from django.urls import path
from . import views
#from .views import register_student

urlpatterns = [

    path('',views.index),
    path('verify_phonenumber/',views.verify_phonenumber),
   # path('register/', register_student, name='student_register'),
    

]
