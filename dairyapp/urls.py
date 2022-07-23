from django.contrib import admin
from django.urls import path
from dairyapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pdf',views.getpdf)  
]