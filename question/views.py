
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Questions
from result.models import Results
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
        # print(i)
        ques=request.POST[i]
        tempQues.append(ques)
        Ques=Questions.objects.filter(id=i)
        # print("this is ",Ques)
        res=Ques[0].answer
        tempRes.append(res)
        if(res==ques):    
            marks+=1
        else:
            wrong+=1
       
    val=Results()
    val.results=[{'questions':form ,'user_answers':tempQues, 'correct_answer':tempRes}]
    val.score=[{'Correct':marks ,'Wrong':wrong}]
    val.auth_id=request.user.id
    val.save()
    return render(request,'result.html',{'marks':marks,'wrong':wrong})       
   
def search(request):
    return render(request, 'result.html')
   
   
   
    # apple=User.objects.get(username=username).pk
    # print("user",apple)
    # current_user = request.auth_User
    # print ("here is current user",current_user.id)

    # print(form)
    # ques=form['question']
    # print(ques)
   
    # if request.method == 'POST':
    #     question = Questions.objects.values_list('id')
    #     for i in question:
    #         print(i)
    #         question=Questions.objects.values_list('id')
    #         u_answer=request.POST.get('answer')
    #         print(u_answer)
    #         u_option=request.POST('option')
    #         if(u_answer==u_option):
    #             correct += 1
    #             return redirect('quiz')
    #         else:
    #             wrong += 1
    #             return redirect('quiz')




        # form.results=request.POST('results')
        # form=Questions.objects.filter().values()[0]
        # print(form)
        # question= Questions.objects.values_list('answer')
        # print(question)
        # form=request.POST
        # print(form)
        # Question = request.POST
        # x= Question
        # print(x)
        # for x in question:
        # print(x)
        # print("this is x",)
        # print(request)
        # print(Question)
        # form=Results()
        # form.results=(1)
        # form.auth_id=('6')
        # form.questions_id=(2)
        # form.user_answer=('a')
        # form.save()



        # questions = Questions.objects.values_list('id')
        # print(questions)
        # for i in questions:
        #     print()
        #     result=request.POST.get({'value'})
        #     no_of_questions = len('id')
        #     ch = random.randint(0, no_of_questions-1)
        #     print(ch)
            
            #print(f'\nQ{i+1} {questions[ch]["question"]}\n')
            # form=request.POST
            # print(form)

            #for option in questions[ch]["option"]:
                #print(option)
                # print(result)
                # answer = input("\nEnter your answer: ")
                # questions= Questions.objects.values_list('answer')
                # if questions[ch]["answer"][0] == answer[0].upper():
                #     print("correct")
                #     score+=1
                # else:
                #     print("incorrect")
                #     del questions[ch]
                #     #print(f'\nFINAL SCORE: {score}')
                #     return render(request,'result.html')
            # else:
            # return render(request,'result.html')

