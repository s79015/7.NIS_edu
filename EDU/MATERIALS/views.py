from django.shortcuts import render
from .models import Lesson




def nav_hor(request):
    lessons = Lesson.objects.all()
    result = {}
    for lesson in lessons:
        result[str(lesson.course_name.subject_name)] = {}
        
       
    for lesson in lessons:
        result[str(lesson.course_name.subject_name)][str(lesson.course_name)] = []
    print(result)
    for lesson in lessons:
        result[str(lesson.course_name.subject_name)][str(lesson.course_name)].append(str(lesson.name))   
    
    context = {'lessons':result}
   
    return render(request, 'MATERIALS/materials_main.html', context)




def content(request):
    lesson= Lesson.objects.last()
    videofile= lesson.lecture_video
    context = {'video':videofile}
    return render(request, 'MATERIALS/materials_main.html', context)