from django.urls import path, include
from .views import *

urlpatterns = [
    #path('',index,name='index'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('doctors/', doctors, name='doctors'),
    path('contact/', contact, name='contact'),
    path('department/', department, name='department'),

    path('variables/', variables, name='variable'),    
    path('tags/', tags, name='tags'),  
    path('tags1/', tags1, name='tags1'),
    path('inheritance/', inheritance, name='inheritance'),
]
