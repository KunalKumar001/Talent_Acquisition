from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Questions
from result.models import Results
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
import random 


def quiz(request):
    result=Questions.objects.all().order_by('?')[:25]
    return render(request,'quiz.html',{'result':result})

def result(request):
    form=request.POST.getlist('question')
    marks=0
    wrong=0
    tempQues=[]
    tempRes=[]
    for i in form:
        if i in request.POST:
            ques=request.POST[i]
            tempQues.append(ques)
            Ques=Questions.objects.filter(id=i)
            res=Ques[0].answer
            tempRes.append(res)
            if(res==ques):    
                marks+=1
            else:
                wrong+=1
       
    val=Results()
    val.results=[{'questions':form ,'user_answers':tempQues, 'correct_answer':tempRes}]
    val.score=[{'correct':marks ,'wrong':wrong}]
    val.auth_id=request.user.id
    val.save()
    return render(request,'result.html',{'marks':marks,'wrong':wrong})


def timezon(request):
    return render(request,'quiz.html')