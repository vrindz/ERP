from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('verify_phonenumber/',views.verify_phonenumber),

]
