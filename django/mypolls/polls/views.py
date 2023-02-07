from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    question_list = Question.objects.all().order_by('-pub_date')
    return render(request, 'polls/index.html', {'question_list': question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    #어떤 질문인지 가지고 옴
    question = get_object_or_404(Question, id=question_id)

    #radio button, default 값이 없기 때문에 오류가 날 수 있어요.
    try:
        select_choice = question.choice_set.get(id=request.POST['choice'])
        # 질문 객체에 연결된 항목객체 중 get 조건에 맞는 것을 가져 옴

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':'아무것도 입력하지 않았습니다.'})
    else:
        select_choice.votes += 1
        select_choice.save() #DB값 반영
    return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/result.html', {'question': question})