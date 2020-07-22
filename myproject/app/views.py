from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/signin.html', context=my_dict)

def something(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/signup.html', context=my_dict)

def everything(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/forgot.html', context=my_dict)

def anything(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/details.html', context=my_dict)

def nothing(request):
    my_dict = {'insert_me' : "Hello World"}
    return render (request, 'first_app/page3.html', context=my_dict)