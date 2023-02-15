from django.contrib import admin

# Register your models here.

from .models import Quiz, Question, FreeTextAnswer, MultipleChoiceAnswer, UserAnswers
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
 

class QuizAdmin(admin.ModelAdmin):
    
     list_display = ('name',)
     ordering = ('name',)
    #  search_fields = ('name')


class QuestionAdmin(admin.ModelAdmin):
     # list_display = [field.name for field in Question._meta.get_fields()]
     list_display = ['quiz_id', 'question_text', 'hash_name']
     ordering = ('quiz_id',)

class FreeTextAnswerAdmin(admin.ModelAdmin):
     list_display = [field.name for field in FreeTextAnswer._meta.get_fields()]
     ordering = ('question',)

class MultipleChoiceAnswerAdmin(admin.ModelAdmin, DynamicArrayMixin):
     list_display = [field.name for field in MultipleChoiceAnswer._meta.get_fields()]
     ordering = ('question',)
     

class UserAnswersAdmin(admin.ModelAdmin):
     list_display = [field.name for field in UserAnswers._meta.get_fields()]
     ordering = ('user_name',)
     



admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FreeTextAnswer, FreeTextAnswerAdmin)
admin.site.register(MultipleChoiceAnswer, MultipleChoiceAnswerAdmin)
admin.site.register(UserAnswers, UserAnswersAdmin)