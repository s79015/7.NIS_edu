from django.shortcuts import get_object_or_404, render, redirect
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



def display_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Test, pk=quiz_id)
    # fetch ALL of the questions to find current and next question
    questions = quiz.question_set.all()
    current_question, next_question = None, None
    for ind, question in enumerate(questions):
        if question.pk == question_id:
            current_question = question
            if ind != len(questions) - 1:
                next_question = questions[ind + 1]

    return render(
        request,
        "quizzes/display.html",
        {"quiz": quiz, "question": current_question, "next_question": next_question},
    )


def grade_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = getattr(question, "multiplechoiceanswer", None) or getattr(question, "freetextanswer")
    is_correct = answer.is_correct(request.POST.get("answer"))
    return render(
        request,
        "quizzes/partial.html",
        {"is_correct": is_correct, "correct_answer": answer.correct_answer},
    )