from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory
from datetime import datetime
from django.core.exceptions import ValidationError
import re

from quizz.models import Score
from quizz.forms import QuizEntryForm
from quizz.quiz_api_service import get_quiz_data


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

            # QuizResultSubmissionForm = modelform_factory(QuizData, exclude=[])
            return render(request, "quiz.html",
                          {"quiz_questions": quiz_data['questions'],
                           "quiz_information": quiz_data['information']})
    else:
        form = QuizEntryForm()

    return render(request, "index.html", {"players": Score.objects.order_by('-score')[:15],
                                          "danas": today,
                                          "form": form})


def start(request):
    return render(request, "quiz.html")


def submit_results(request):
    if request.method == "POST":
        # form = QuizSubmissionForm(request.POST)
        # if quizSubmission.is_valid():
        #     result = get_results(form.cleaned_data)
        # QuizzForm = modelform_factory()
            quiz_data = []
            return render(request, "results.html", {"quiz": quiz_data})
    else:
        form = QuizEntryForm()

    return redirect('index')
