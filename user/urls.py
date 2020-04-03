from django.urls import path
from . import views


urlpatterns=[ 
    path("",views.index, name="index"),
    path("register",views.register, name="register"),
    path("welcome",views.welcome, name="welcome"),
    path("verify/<token>",views.verify,name="verify")
    # path("welcome/verify/<token>",views.welcome,name="")
]
