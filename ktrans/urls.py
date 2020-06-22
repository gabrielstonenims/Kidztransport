from django.urls import path

from . import views
from .views import CreateDriver,RegisterStudent


urlpatterns =[
    path('',views.home,name='home'),
    path('student_register/',RegisterStudent.as_view(),name='student_register'),
    path('about/',views.about,name='about'),
    path('register_driver/',CreateDriver.as_view(),name='register_driver'),
    path('drivers/',views.drivers,name='drivers'),
    path('our_drivers/',views.our_drivers,name='our_drivers'),
    path('parents/',views.parents,name='parents'),
    path('service_areas/',views.service_areas,name='service_areas'),
    path('team/',views.theteam,name='team'),
    path('contact/',views.contact,name='contact')
]