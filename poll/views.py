from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Question, Choice
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def index(request):
    "Homepage view"
    recent_question_list = Question.objects.order_by('-pub_date')[:5]
    response = ", ".join([q.question for q in recent_question_list])
    content = {"recent_question_list": recent_question_list}
    return render(request, "poll/index.html", content )

def question_detail(request, question_id):
    "View that displays question details"
    question = get_object_or_404(Question, pk=question_id)
    content = {'question_detail': question}
    return render(request, 'poll/question_detail.html', content)


def results(request, question_id):
    "View that displays the answers/choices for each question"
    question = get_object_or_404(Question, pk=question_id)
    content = {'question_detail': question}
    return render(request, 'poll/results.html', content)

def vote(request, question_id):
    "This view shows a form to vote an answer for each question"
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = get_object_or_404(Choice, pk=request.POST['choice'])
    if KeyError:
        content = {'question_detail': question,
                   'error_message': "you didn't select a choice"}
        return render(request, 'poll/detail.html', content)
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question_id, )))
