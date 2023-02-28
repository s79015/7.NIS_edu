from django.contrib import admin

# Register your models here.

from .models import Quiz, Question, FreeTextAnswerRus, FreeTextAnswerKaz, MultipleChoiceAnswerRus, MultipleChoiceAnswerKaz,UserAnswers, QuestionHash, Subject
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.safestring import mark_safe




class QuizAdmin(admin.ModelAdmin):
    
     list_display = ('name_rus', 'name_kaz')
     ordering = ('name_rus',)
    #  search_fields = ('name')


class QuestionAdmin(admin.ModelAdmin):
     # list_display = [field.name for field in Question._meta.get_fields()]
     list_display = ['quiz_id', 'question_text_rus', 'hash_name_rus', 'question_img']
     ordering = ('question_text_rus',)

   

class FreeTextAnswerRusAdmin(admin.ModelAdmin):
     list_display = [field.name for field in FreeTextAnswerRus._meta.get_fields()]
     ordering = ('question',)
     exclude = ('correct_answer_kaz',)

class FreeTextAnswerKazAdmin(admin.ModelAdmin):
     list_display = [field.name for field in FreeTextAnswerKaz._meta.get_fields()]
     ordering = ('question',)
     exclude = ('correct_answer_rus',)

class MultipleChoiceAnswerRusAdmin(admin.ModelAdmin, DynamicArrayMixin):
     list_display = [field.name for field in MultipleChoiceAnswerRus._meta.get_fields()]
     ordering = ('question',)
     exclude = ('correct_answer_kaz',)

class MultipleChoiceAnswerKazAdmin(admin.ModelAdmin, DynamicArrayMixin):
     list_display = [field.name for field in MultipleChoiceAnswerKaz._meta.get_fields()]
     ordering = ('question',)
     exclude = ('correct_answer_rus',)
     

class UserAnswersAdmin(admin.ModelAdmin):
     list_display = [field.name for field in UserAnswers._meta.get_fields()]
     ordering = ('user_name',)
     
class QuestionHashAdmin(admin.ModelAdmin):
     list_display = ['hash_name_rus', 'hash_name_kaz']
     ordering = ('hash_name_rus',)
     



class SubjectAdmin(admin.ModelAdmin):
     # list_display = [field.name for field in Question._meta.get_fields()]
     list_display = ['name_rus', 'name_kaz']
     ordering = ('name_rus',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FreeTextAnswerRus, FreeTextAnswerRusAdmin)
admin.site.register(FreeTextAnswerKaz, FreeTextAnswerKazAdmin)
admin.site.register(MultipleChoiceAnswerRus, MultipleChoiceAnswerRusAdmin)
admin.site.register(MultipleChoiceAnswerKaz, MultipleChoiceAnswerKazAdmin)
admin.site.register(UserAnswers, UserAnswersAdmin)
admin.site.register(QuestionHash, QuestionHashAdmin)
admin.site.register(Subject, SubjectAdmin)


