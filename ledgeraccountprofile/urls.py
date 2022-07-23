from django.contrib import admin
from django.urls import path
from ledgeraccountprofile import views

urlpatterns = [
    path('',views.index,name='index'),
]