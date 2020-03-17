from django.shortcuts import render
from django.http import HttpResponse
from . models import typ


# Create your views here.
def index(request):
    data= typ.object.all()
    return render(request,"index.html")
