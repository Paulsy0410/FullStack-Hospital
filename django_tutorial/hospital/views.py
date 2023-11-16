from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments ,Doctors

from .forms import BookingForm


# Create your views here.

# def index(request): 
#     return (HttpResponse('hello world'))

# def home(request): 
#     return(HttpResponse("home page"))

# def about(request): 
#     return(HttpResponse("about page"))

# def booking(request): 
#     return(HttpResponse("booking page"))

# def doctors(request): 
#     return(HttpResponse("doctors page"))

# def contact(request): 
#     return(HttpResponse("contact page"))

# def department(request): 
#     return(HttpResponse("department page"))


#template view

def index(request): 
    return render(request,'index.html')

def home(request): 
    return render(request,'1_home.html')

def about(request): 
    return render(request,'2_about.html')

def booking(request): 
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, '8_confirmation.html')
    form=BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'3_booking.html',dict_form)

def doctors(request): 
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'6_doctors.html',dict_docs)

def contact(request): 
    return render(request,'4_contact.html')

def department(request): 
     dict_dept={
        'dept': Departments.objects.all()
    }
     return render(request,'5_department.html',dict_dept)



#variables and tags

def variables(request): 
    person={
        'name':'john',
        'age':34 ,
        'place':'kakkanaad'

    }
    return render(request,'variables.html',person)

def tags(request): 
    numbers= {
            'num':0
        }
    return render(request,'tags_if.html',numbers)



def tags1(request): 
    numbers1= {
            'num1':[1,2,3,4,5,6,7,8,9,10]
        }
    return render(request,'tags_for.html',numbers1)


#inheritance

def inheritance(request): 
    return render(request,'INHERITANCE.HTML')