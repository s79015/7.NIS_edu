from django.contrib import admin

# Register your models here.

from .models import Test, Course, Subject

 

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