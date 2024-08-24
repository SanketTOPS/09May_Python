from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('appointment/',views.appointment),
   path('calltoaction/',views.calltoaction),
   path('classes/',views.classes),
   path('contact/',views.contact),
   path('facility/',views.facility),
   path('testimonial/',views.testimonial),
   path('team/',views.team),

   

]