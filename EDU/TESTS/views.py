from django.shortcuts import render
from .models import Test, Test_error_answers

import random


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
    

    tests= Test.objects.filter(name='Test 1').all()
    test_questions = {}
    for test in tests:
        test_questions[str(test.name)] = {}
        

    for test in tests:
        test_questions[str(test.name)][str(test.test_question)] = []
        test_questions[str(test.name)][str(test.test_question)].append(str(test.test_answer))

    for test in tests:
        print(test.test_question)
        error_answers = Test_error_answers.objects.filter(test_question=str(test.id)).values_list('test_error_answer', flat=True)
        # print(error_answers)
        for error in list(error_answers):
            print(test_questions[str(test.name)][str(test.test_question)])
            test_questions[str(test.name)][str(test.test_question)].append(error)
        
        random.shuffle(test_questions[str(test.name)][str(test.test_question)])
        print(test_questions[str(test.name)][str(test.test_question)])
   
    context = {'test':result, 'math': Tests[0].test_question, 'test_questions': test_questions[test.name]}
   
    return render(request, 'TESTS/test_main.html', context)




def content(request):
    tests= Test.objects.all()
    result = {}
    for test in tests:
        result[str(test.name)] = {}
        

    for test in tests:
        result[str(test.name)][str(test.test_question)] = []
        result[str(test.name)][str(test.test_question)].append(str(test.answer))

    for test in tests:
        error_answers = test.Test_error_answers_set.all().values_list()
        
        result[str(test.name)][str(test.test_question)].append(str(error_answers))
    

    context = {'test_content':result}
    return render(request, 'TESTS/test_main.html', context)