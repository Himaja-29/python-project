import string
import random

from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import *
from django.shortcuts import render

def hello1(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")

def newhomepage(request):
    return render(request,'newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage.html')


def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'print_to_console.html',a1)



def randomcall(request):
    return render(request,'randomotpgenerator.html')


def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input:{user_input}')
        a2=int(user_input)
        ran1=''.join(random.sample(string.digits,k=a2))
    a1={'ran1':ran1}
    return render(request,'randomotpgenerator.html',a1)
def getdate1(request):
    return render(request,'get_date.html')
import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form =IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value =form.cleaned_data['date_value']
            updated_date=date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
            return render(request,'get_date.html',{'form':form})

def registerloginfunctioncall(request):
            return render(request, 'register.html')

import datetime
from.models import*
from django.shortcuts import render,redirect
def registerloginfunction(request):
  if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      password=request.POST.get('password')
      phonenumber=request.POST.get('phonenumber')
      if himaja.objects.filter(email=email).exists():
          return HttpResponse("Email already registered.Choose a different email.")
      himaja.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
      return redirect('newhomepage')
  return render(request,'register.html')
import requests
def weatherpagecall(request):
    return render(request,'weatherinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'b62dc56a194820966f2b40265047353f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherinput.html', {'error_message': error_message})

def submitfunctioncall(request):
    return render(request, 'submit.html')
import datetime
from.models import*
from django.shortcuts import render,redirect
def submitfunction(request):
  if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      phonenumber=request.POST.get('phonenumber')
      suggestions=request.POST.get('suggestions')
      sharu.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
      return HttpResponse("You were submitted successfully.")
      return redirect('newhomepage')
  return render(request,'submit.html')

def feedbackcalling(request):
    return render(request,'feedbackform.html')

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feedbackform

def feedbackfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        feedback_message = request.POST.get('feedback_message')
        tosend=feedback_message+'__this is just a copy__'
        if Feedbackform.objects.filter(email=email).exists():
            return HttpResponse("Email already submitted feedback. Please provide feedback only once.")
        Feedbackform.objects.create(name=name, email=email, phonenumber=phonenumber, feedback_message=feedback_message)
        send_mail(
            'Thank you for contacting',
            tosend,
            '2200030263cseh@gmail.com',
            [email],
            fail_silently=False,
        )

        # return redirect('newHomePage')
    return render(request, 'feedbackform.html')

