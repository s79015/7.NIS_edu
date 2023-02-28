from django.db import models
from django.contrib.postgres import fields
from django.conf import settings

import datetime

from django_better_admin_arrayfield.models.fields import ArrayField


class Subject(models.Model):
    name_rus = models.CharField(max_length=100, null=True, blank=True)
    name_kaz= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_rus
    

class Quiz(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    name_rus = models.CharField(max_length=100, null=True, blank=True)
    name_kaz= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_rus

class QuestionHash(models.Model):
    hash_name_rus = models.CharField(max_length=100, null=True, blank=True)
    hash_name_kaz = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.hash_name_rus


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    hash_name_rus = models.ForeignKey(QuestionHash, on_delete=models.CASCADE, null=True, blank=True)
   
    # prompt = models.CharField(max_length=200)
    question_text_rus = models.CharField(max_length=200, null=True, blank=True)
    question_text_kaz = models.CharField(max_length=200, null=True, blank=True)

    question_solution_rus = models.CharField(max_length=10000,  null=True, blank=True)
    question_solution_kaz = models.CharField(max_length=10000,  null=True, blank=True)
   
    question_img = models.ImageField(null=True, blank=True, upload_to="upload_image/")

    def __str__(self):
        return self.question_text_rus


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    correct_answer_rus = models.CharField(max_length=200, null=True, blank=True)
    correct_answer_kaz = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class FreeTextAnswerRus(Answer):
    case_sensitive = models.BooleanField(default=False)

    def __str__(self):
        return self.correct_answer_rus

    def is_correct(self, user_answer):
        if not self.case_sensitive:
            return user_answer.lower() == self.correct_answer_rus.lower()
        return user_answer == self.correct_answer_rus

class FreeTextAnswerKaz(Answer):
    case_sensitive = models.BooleanField(default=False)

    def __str__(self):
        return self.correct_answer_kaz

    def is_correct(self, user_answer):
        if not self.case_sensitive:
            return user_answer.lower() == self.correct_answer_kaz.lower()
        return user_answer == self.correct_answer_kaz


class MultipleChoiceAnswerRus(Answer):
    # choices = fields.ArrayField(models.CharField(max_length=200, blank=True))
    choices = ArrayField(models.CharField(max_length=200, blank=True))

    def __str__(self):
        return f"{self.correct_answer_rus} from {self.choices}"

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer_rus

class MultipleChoiceAnswerKaz(Answer):
    # choices = fields.ArrayField(models.CharField(max_length=200, blank=True))
    choices = ArrayField(models.CharField(max_length=200, blank=True))

    def __str__(self):
        return f"{self.correct_answer_kaz} from {self.choices}"

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer_kaz

class UserAnswers(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.PROTECT)
    quiz_name = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    quiz_hash_name = models.ForeignKey(QuestionHash, on_delete=models.PROTECT, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True, blank=True)
    user_answer_is_correct = models.BooleanField()
    user_spend_time = models.IntegerField(null=True, blank=True)
    answer_date = models.DateTimeField(default=datetime.datetime.now())


