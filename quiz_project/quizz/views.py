from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import modelform_factory
from datetime import datetime

from quizz.models import Player

# MeetingForm = modelform_factory(Meeting, eclu)

def index(request):
    today = datetime.now().strftime("%d %b, %Y")
    return render(request, "index.html", {"players": Player.objects.all(),
                                          "danas": today})


def start(request):
    return HttpResponse("About me text")


def finish(request):
    return render(request, "results.html")
