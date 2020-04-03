from django.shortcuts import render
from django.http import HttpResponse
from . models import typ

def index(request):
    data= typ.object.all()
    return render(request,"index.html")
