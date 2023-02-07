from django.contrib import admin

# Register your models here.

from .models import Test, Course, Subject, Test_error_answers

class Test_error_answersAdmin(admin.ModelAdmin):
     list_display = ('test_question', 'test_error_answer')
     ordering = ('test_question',)
     search_fields = ('test_question', 'test_error_answer')

class TestAdmin(admin.ModelAdmin):
     list_display = ('course_name', 'name', 'test_question', 'test_answer')
     ordering = ('name',)
     search_fields = ('name', 'course_name')


class CourseAdmin(admin.ModelAdmin):
     list_display = ('subject_name', 'name')
     ordering = ('name',)

class SubjectAdmin(admin.ModelAdmin):
     list_display = ['name']
     ordering = ('name',)
     


admin.site.register(Test, TestAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Test_error_answers, Test_error_answersAdmin)