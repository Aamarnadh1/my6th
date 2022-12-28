from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('<h1>This is my app1 first string1<h1>')

def string2(request):
    return HttpResponse('<h2> This is  my app1 second</h2')    

def string3(request):
    return HttpResponse('<h2> This is  my app1 3rd</h2')    

