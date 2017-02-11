from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[5:]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list': latest_question_list
    }
    output = ', '.join([q.question_text for q in latest_question_list])

    return render(request, 'polls/index.html', context)


def add_a_question(request, question_id):
    return HttpResponse("Add a question")

def current_question(request):
    response = "Question %s"
    return HttpResponse(response % question_id)