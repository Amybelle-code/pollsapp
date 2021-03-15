from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    "Class to create Question model"
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        "A string representation of the model in Django Admin"
        return self.question
    
    def was_published_recently(self):
        """To check if a question was recently published by comparing its pub_date value with the
        current time"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    



class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
