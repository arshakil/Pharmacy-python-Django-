
from django.urls import path
from . import views


urlpatterns = [
    path('',views.add_purchase,name='add_purchase'),
    path('load_medicine/',views.load_medicine,name='load_medicine'),
 
  
]
