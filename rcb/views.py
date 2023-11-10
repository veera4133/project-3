from django.shortcuts import render
from django.http import HttpResponse
def virat(request):
    return render(request,'virat.html')

def abd (request):
    return HttpResponse('<h1>mr360</h1>')
