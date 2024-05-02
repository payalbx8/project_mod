from django.shortcuts import render,HttpResponse
from django.template import loader
from datetime import datetime
from app_mod.models import contact
from app_mod import forms 
from django.contrib import messages



def index(request):

    data = contact.objects.all()
    print(data)
    context = {'data' : data}

   
    return render(request,'index.html',context)
       
def contacts(request):
    if request.method =="POST":
        form = forms.InfoRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your message has been sent !")
       
       
    return render(request,'contact.html')


    
