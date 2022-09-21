from django.shortcuts import render, redirect
from datetime import datetime
from django.core.exceptions import ValidationError
import re

from quizz.models import QuizResult
from quizz.forms import QuizEntryForm
from quizz.quiz_api_service import get_quiz_data, process_quiz_results


def validate_username(value):
    if re.match("^[a-zA-Z0-9_]+$", value):
        return value
    else:
        raise ValidationError("This field accepts characters, numbers")


def index(request):
    today = datetime.now().strftime("%d %b, %Y")
    if request.method == "POST":
        form = QuizEntryForm(request.POST)
        if form.is_valid():
            quiz_data = get_quiz_data(form.cleaned_data)

            return render(request, "quiz.html",
                          {"quiz_questions": quiz_data['questions'],
                           "quiz_information": quiz_data['information'],
                           "quiz_solution": quiz_data['solution']
                           })
    else:
        form = QuizEntryForm()

    return render(request, "index.html", {"players": QuizResult.objects.order_by('-score')[:15],
                                          "danas": today,
                                          "form": form})


def start(request):
    return render(request, "quiz.html")


def submit_results(request):
    if request.method == "POST":
        results = request.POST.dict()
        quiz_score_data = process_quiz_results(results)
        return render(request, "results.html", {"quiz_score": quiz_score_data,
                                                "players": QuizResult.objects.order_by('-score')[:15]})
    else:
        form = QuizEntryForm()

    return redirect('index')
