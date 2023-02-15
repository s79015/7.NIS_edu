from django.db import models
from django.contrib.postgres import fields
from django.conf import settings

import datetime

from django_better_admin_arrayfield.models.fields import ArrayField



    

class Quiz(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QuestionHash(models.Model):
    hash_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.hash_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    hash_name = models.ForeignKey(QuestionHash, on_delete=models.CASCADE, null=True, blank=True)
   
    # prompt = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)

    question_solution = models.CharField(max_length=10000,  null=True, blank=True)
   


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=200)

    class Meta:
        abstract = True


class FreeTextAnswer(Answer):
    case_sensitive = models.BooleanField(default=False)

    def __str__(self):
        return self.correct_answer

    def is_correct(self, user_answer):
        if not self.case_sensitive:
            return user_answer.lower() == self.correct_answer.lower()
        return user_answer == self.correct_answer


class MultipleChoiceAnswer(Answer):
    # choices = fields.ArrayField(models.CharField(max_length=200, blank=True))
    choices = ArrayField(models.CharField(max_length=200, blank=True))

    def __str__(self):
        return f"{self.correct_answer} from {self.choices}"

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer

class UserAnswers(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.PROTECT)
    quiz_name = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    quiz_hash_name = models.ForeignKey(QuestionHash, on_delete=models.PROTECT, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True, blank=True)
    user_answer_is_correct = models.BooleanField()
    user_spend_time = models.IntegerField(null=True, blank=True)
    answer_date = models.DateTimeField(default=datetime.datetime.now())


