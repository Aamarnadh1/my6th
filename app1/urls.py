from django.urls import path
from app1.views import *
app_name='somthing'
urlpatterns=[
     path('string1/',string1,name='string1'),
     path('string2/',string2,name='string2'),
     path('string3/',string3,name='string3')
   
   
]