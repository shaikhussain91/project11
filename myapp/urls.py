from django.urls import path

from .views import *

app_name='myapp'

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('bootcamp/', bootcamp, name='bootcamp'),
    path('requestcallback/', requestcallback, name='requestcallback'),
    path('signin/', signin, name='signin'),
    path('form/', form , name='form'),
    path('bootform/', bootform , name='bootform'),
    path('freelearning/', freelearning , name='freelearning'),
]
