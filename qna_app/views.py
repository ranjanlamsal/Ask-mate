from django.shortcuts import render
from .models import QuestionModel

# Create your views here.
def question(requests):
    Question = QuestionModel.objects.all()
    return render(requests,'question.html',{'question':Question})