from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q

from .forms import GetCodeForm
from .models import Code
from polls.models import Question, Choice
import random
from django.utils.safestring import mark_safe

def get_code(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetCodeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # form.cleaned_data - dictionary with data
            selected_choice = GetCodeForm.question.choice_set.all()[int(form.cleaned_data["choice_field"])]
            question = GetCodeForm.question
            #return HttpResponse(str(selected_choice))
            #return HttpResponse(str(GetCodeForm.question))
            return HttpResponseRedirect(reverse('polls:test', args=(question.id, selected_choice.id,)))
    # if a GET (or any other method) we'll create a blank form
    else:
        q = random.choice(Question.objects.filter(active=True))
        GetCodeForm.question = q
        choices = []
        order = 0
        for c in q.choice_set.all():
            choices.append((order, c.choice_text))
            order += 1
        GetCodeForm.base_fields["choice_field"].label = mark_safe("<strong>" + q.question_text + "</strong>")
        GetCodeForm.base_fields["choice_field"].choices = choices  
        form = GetCodeForm()
    return render(request, 'accesscodes/get_code.html', {'form': form})

class IndexView(generic.ListView):
    template_name = 'accesscodes/index.html'
    context_object_name = 'code_list'

    def get_queryset(self):
        """
        """
        return Code.objects.all() 

def dump_codes(request):
    codes = Code.objects.filter(
        Q(valid_from=None) | Q(valid_from__lte=timezone.now()),
        Q(valid_to=None) | Q(valid_to__gte=timezone.now())
    )
    data = [
        {
            'code_input': c.code_input,
            'code_number': c.code_number,
            'valid_from': c.valid_from,
            'valid_to': c.valid_to,
            'username': None if not c.user else c.user.username,
        } for c in codes
    ]
    return JsonResponse(data, safe=False)


