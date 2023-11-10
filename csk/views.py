from django.shortcuts import render
from django.http import HttpResponse
def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1>mr ipl</h1>')