from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from talent_acquisition.settings import EMAIL_HOST_USER
import uuid 
from django.template.loader import get_template
from django.template import Context
from user.models import Token


#this is index page
def index(request):
    return render(request,'register.html')

#this is user registration page 
def register(request):
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['first_name']
        email      = request.POST['email']
        password   = request.POST['first_name']
        token =  uuid.uuid4().hex[:15].upper()
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            print('user created')
            username=username
            password=password
            user = auth.authenticate(username=username,password=password)  
            auth.login(request,user)
            verifytoken = Token()             
            verifytoken.auth_id=request.user.id             
            verifytoken.token = token                          
            verifytoken.save()


#sending mail to the user  
            recievers=[]
            htmly     = get_template('email.html')
            # for user in User.objects.all():
            recievers.append(user.email) 
            
            html_content = htmly.render({ 'username': user.username,'token':token})
            msg = EmailMultiAlternatives('welcome to navadhiti','', email,recievers)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        return redirect('welcome') 
    
    else:
        return render(request,'register.html')




#this is welcome page
def welcome(request):
    return render(request,'welcome.html')



def verify(request,token):
    token1= Token.objects.filter(token = token)     
    print(token1)     
    if(token1 ==  token):         
        return redirect('welcome')     
    else:         
        return render(request,'welcome.html')



