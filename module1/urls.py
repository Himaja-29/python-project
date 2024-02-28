from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [
    path('hello1/',hello1, name='hello'),
    path('', newhomepage, name='home'),
    path('package/',travelpackage,name = 'package'),
    path('print/',print_to_console, name= 'print_to_console'),
    path('p/',print1,name='print'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randologic/',randomlogic,name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='get_date'),
    path('register1/',registerloginfunction,name='registerloginfunction'),
    path('register/', registerloginfunctioncall, name='registerloginfunctioncall'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('submitfunctioncall/',registerloginfunction,name='submitfunctioncall'),
    path('submitfunction/', registerloginfunctioncall, name='submitfunction'),
    path('feedbackcalling/', feedbackcalling, name='feedbackcalling'),
    path('feedbackfunction/', feedbackfunction, name='feedbackfunction'),
]