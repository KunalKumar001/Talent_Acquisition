from django.db import models 
from django.contrib.auth.models import User   

class Token(models.Model):     
    auth=models.ForeignKey('auth.User', on_delete=models.CASCADE,)     
    token=models.CharField(max_length=100)      
    class Meta:         
        db_table = 'token'
        



