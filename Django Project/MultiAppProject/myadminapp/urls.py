from django.contrib import admin
from django.urls import path,include
from myadminapp import views

urlpatterns = [
   path('index/',views.index),
]