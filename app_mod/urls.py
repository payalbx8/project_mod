from django.contrib import admin
from django.urls import path
from app_mod import views

urlpatterns = [
    path("",views.index,name='app_mod'),
    path("contact",views.contacts,name='contact')
]