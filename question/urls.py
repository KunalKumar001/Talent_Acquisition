from django.urls import path
from . import views


urlpatterns=[
    path("quiz",views.quiz,name="quiz"),
    path("result",views.result,name="result"),
    #path("result",views.checkAnswer,name="checkAnswer"),

]