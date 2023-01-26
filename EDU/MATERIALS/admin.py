from django.contrib import admin

# Register your models here.

from .models import Subject, Course, Lesson

 

class LessonAdmin(admin.ModelAdmin):
     list_display = ('course_name', 'name', 'lecture_text', 'lecture_video')
     ordering = ('name',)
     search_fields = ('name', 'course_name')


class CourseAdmin(admin.ModelAdmin):
     list_display = ('subject_name', 'name')
     ordering = ('name',)

class SubjectAdmin(admin.ModelAdmin):
     list_display = ['name']
     ordering = ('name',)
     


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)