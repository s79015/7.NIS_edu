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

    
class Lesson(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lecture_text = models.CharField(max_length=100000, blank=True)
    lecture_picture = models.ImageField(upload_to='upload_image', blank=True)
    lecture_video = models.FileField(upload_to='upload_video', verbose_name="", blank=True)
    def __str__(self):
        return self.name
