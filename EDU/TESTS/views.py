from django.shortcuts import render
from .models import Test




def nav_hor(request):
    Tests = Test.objects.all()
    result = {}
    for test in Tests:
        result[str(test.course_name.subject_name)] = {}
        
       
    for test in Tests:
        result[str(test.course_name.subject_name)][str(test.course_name)] = []
    print(result)

    for test in Tests:
        result[str(test.course_name.subject_name)][str(test.course_name)].append(str(test.name))   
    
    context = {'test':result, 'math': Tests[0].test_question}
   
    return render(request, 'TESTS/test_main.html', context)




def content(request):
    lesson= Lesson.objects.last()
    videofile= lesson.lecture_video
    context = {'video':videofile}
    return render(request, 'MATERIALS/materials_main.html', context)