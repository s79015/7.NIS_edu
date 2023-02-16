from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Quiz, Question, UserAnswers


class IndexView(generic.ListView):
    model = Quiz
    template_name = "QUIZ/index.html"


def display_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = quiz.question_set.first()
    return redirect(reverse("quiz:display_question", kwargs={"quiz_id": quiz_id, "question_id": question.pk}))


def display_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
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
        "QUIZ/display.html",
        {"quiz": quiz, "question": current_question, "next_question": next_question},
    )


def grade_question(request, question_id, lg):
    question = get_object_or_404(Question, pk=question_id)
    if lg == 'rus':
        answer = getattr(question, "multiplechoiceanswerrus", None) or getattr(question, "freetextanswerrus")
        correct_answer = answer.correct_answer_rus
    elif lg == 'kaz':
        answer = getattr(question, "multiplechoiceanswerkaz", None) or getattr(question, "freetextanswerkaz")
        correct_answer = answer.correct_answer_kaz
    else:
        answer = ''
        correct_answer = ''

    is_correct = answer.is_correct(request.POST.get("answer"))
    if request.user.is_authenticated:
        print(request.user)
        u = UserAnswers(user_name = request.user, 
                        quiz_name = question.quiz,     
                        quiz_hash_name = question.hash_name_rus,
                        question = question,
                        user_answer_is_correct = is_correct,
                        user_spend_time = 10
                    )
        u.save()
    return render(
        request,
        "QUIZ/partial.html",
        {"is_correct": is_correct, "correct_answer": correct_answer},
    )


