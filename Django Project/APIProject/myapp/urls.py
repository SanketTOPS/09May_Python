from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getid/<int:id>',views.getid),
    path('savedata/',views.savedata),
    path('updatedata/<int:id>',views.updatedata),
    path('deletedata/<int:id>',views.deletedata),
]
