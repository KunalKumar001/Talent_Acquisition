from django.db import models
from jsonfield import JSONField
# Create your models here.

class Results(models.Model):
    results = JSONField()
    score = JSONField()
    user_answer=models.CharField(max_length=200)
    auth=models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    


    class Meta:
        db_table = 'results'