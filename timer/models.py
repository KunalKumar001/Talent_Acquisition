from django.db import models

# Create your models here.
class Timer(models.Model):
    auth=models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    updated = models.DateTimeField(auto_now=True,blank=True)

    class Meta:
        db_table = 'timer'
