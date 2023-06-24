from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
import json


# Create your views here.
def index(request):
    return HttpResponse("Home Page")
def verify_phonenumber(request):
    global res
    try:
        phonenumber = request.GET.get('id',)
        
        student = Students.objects.get(phone=phonenumber)
    except Students.DoesNotExist:
    
        res = {"message":"Student doesn't exist"}
        # The phone number does not exist in the database.
    except:
    
        res = {"message":"Something went wrong"}
    else:
        res = {"message":"Student with phone exists..Please add another"}
    
    return HttpResponse(json.dumps(res), content_type='application/json')
 
