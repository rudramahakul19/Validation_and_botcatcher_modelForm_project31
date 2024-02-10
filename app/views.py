from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def create_student(request):
    ESFO=Studentform()
    d={'ESFO':ESFO}

    if request.method == 'POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('student inserted successfully')
        else:
            return HttpResponse('Invalid')
    return render(request,'create_student.html',d)