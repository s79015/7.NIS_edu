from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class Test(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    test_question = models.CharField(max_length=100000, blank=True)
    test_answer = models.CharField(max_length=100000, blank=True)
    def __str__(self):
        return self.test_question


class Test_error_answers(models.Model):
    test_question = models.ForeignKey(Test, on_delete=models.CASCADE)
    test_error_answer = models.CharField(max_length=100000, blank=True)
    def __str__(self):
        return self.test_error_answer
