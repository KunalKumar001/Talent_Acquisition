from django.db import models

class QuestionType(models.Model):
    is_active=models.BooleanField(default=False)
    percentage=models.IntegerField()
    question_type=models.CharField(max_length=200)
    class Meta:
        db_table = 'question_types'
    