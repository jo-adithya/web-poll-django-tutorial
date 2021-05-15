from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_questions': latest_questions, }
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
    return HttpResponse(f'You are looking at the results of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')
