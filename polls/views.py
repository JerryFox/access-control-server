from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

import random
import datetime


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            active=True
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:test', args=(question.id,selected_choice.id,)))

def random_vote(request): 
    random_question = random.choice(Question.objects.filter(active=True))
    return HttpResponseRedirect(reverse('polls:vote', args=(random_question.id,)))

def test_choice(request, question_id, choice_id): 
    now = datetime.datetime.now()
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    try: 
        ipk = question.choice_set.get(correct_choice=True).pk 
    except: 
        ipk = -1
    correct_choice = get_object_or_404(Choice, pk=ipk)
    if correct_choice.id == int(choice_id): 
        answer_is = "correct" 
    else: 
        if choice in question.choice_set.all(): 
            answer_is = "wrong"
        else: 
            answer_is = "out of question"
    choices = ""
    choices = "<ul>\n" 
    for c in question.choice_set.all(): 
        choices += "<li>" + str(c.id) + " " + c.choice_text + "</li>\n"
    choices += "</ul>\n"
    html = """<html><body>
<h3>{} {}</h3>
{}
Your answer is {}<br />
The right choice: {} {}
</body></html>
""".format(
        question.id, 
        question.question_text, 
        choices, 
        answer_is, 
        correct_choice.id, 
        correct_choice.choice_text)
    return HttpResponse(html)

