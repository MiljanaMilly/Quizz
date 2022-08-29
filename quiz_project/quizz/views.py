from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.forms import modelform_factory
from datetime import datetime
from django.core.exceptions import ValidationError
import re

from quizz.models import QuizEntry, Score

QuizEntryForm = modelform_factory(QuizEntry, exclude=[])


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
            # call api caller function
            return redirect("start")

    else:
        form = QuizEntryForm()

    return render(request, "index.html", {"players": Score.objects.order_by('-score')[:15],
                                          "danas": today,
                                          "form": form})


def start(request):
    return render(request, "quiz.html")


def finish(request):
    return render(request, "results.html")
