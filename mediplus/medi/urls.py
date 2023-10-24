from medi import views
from django.urls import path

urlpatterns = [
    
 path('', views.index, name='index'),
 path('contact', views.contact, name='contact'),
 path('about', views.about, name='about'),
 path('services', views.services, name='services'),
 path('service_details/<str:slug>',views.service_details, name="service_details"),
 path('gallery', views.gallery, name='gallery'),

 
 ]