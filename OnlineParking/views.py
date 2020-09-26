from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import *

def signup(request) :
    return render(request,"signup.html")

def signin(request) :
    return render(request,"signin.html")

def forgot(request) :
    return render(request,"forgot.html")

def details(request) :
    return render(request,"details.html")

def fare(request) :
    return render(request,"details.html")

def booking(request) :
    return render(request,"booking.html")

def signup_submit(request) :
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        dateOfBirth = request.POST['dateOfBirth']
        if(password == confirmPassword) :
            try :
                signUp(username=username, email=email, password=password, dateOfBirth=dateOfBirth).save()
                return render(request,"fare.html", {email:email})
            except Exception as e :
                messages.add_message(request, messages.INFO, 'Email id is already registered')
        else :
            messages.add_message(request, messages.INFO, 'Password and Confirm Password are not same..')
            return render(request, "signin.html")
    messages.add_message(request, messages.INFO, 'Email id is already registered')
    return render(request, "signin.html")

def signin_submit(request) :
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try :
            data = signUp.objects.filter(email=email, password=password)
        except Exception as e :
            messages.add_message(request, messages.INFO, 'Invalid Credentials..')
        if data: 
            return render(request,"fare.html", {email:email})
        messages.add_message(request, messages.INFO, 'Invalid Credentials..')
    return render(request,"signin.html")

def forgot_submit(request) :
    if request.method == 'POST':
        email = request.POST['email']
        dateOfBirth = request.POST['dateOfBirth']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if(password == confirmPassword) :
            try :
                data = signUp.objects.get(email=email, dateOfBirth=dateOfBirth)
                if data:
                    data.password=password
                    data.save()
                    return render(request,"fare.html", {email:email})
            except Exception as e:
                messages.add_message(request, messages.INFO, 'Unsuccessful..')
        else :
            messages.add_message(request, messages.INFO, 'Password and Confirm Password are not same..')
            return render(request,"forgot.html")
        
        
    return render(request,"forgot.html")

def details_submit(request) :
    if request.method == 'POST':
        vehicle = request.POST['vehicle']
        VehicleNumber = request.POST['VehicleNumber']
        date = request.POST['date']
        time = request.POST['time']
        place = request.POST['place']
        phone = request.POST['phone']
        try :
            data = book(vehicle=vehicle, VehicleNumber=VehicleNumber, date=date, time=time, place=place, phone=phone).save()
        except Exception as e:
            return render(request, "details.html")
        return render(request,"booking.html", {data : data})
    return render(request, "details.html")