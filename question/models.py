from django.db import models
from jsonfield import JSONField

class Questions(models.Model):
    title=models.CharField(max_length=200)
    option=JSONField()
    answer=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True)
    option_available = models.BooleanField(default =False)
    questionstyp=models.ForeignKey('typ.QuestionType', on_delete=models.CASCADE,)

    
    class Meta:
        db_table = 'questions'