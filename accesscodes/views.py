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
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import User, Group
import datetime

def gen_code(length=5): 
    """new unique numeric keypad code generating"""
    while True: 
        newcode = ""
        for i in range(length): 
            newcode += random.choice("0123456789")
        if not Code.objects.filter(code_input="k").filter(code_number=newcode): 
            return newcode
        newcode = ""

@xframe_options_exempt
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
            # MAIN LOGIC
            # if user email is not in database insert it
            # if answer is correct generate the access code
            # send email
            users = User.objects.filter(email=form.cleaned_data["user_email"])
            if users: 
                # user with this email exists
                u = users[0]
            else: 
                # create new user
                u = User()
                u.email = form.cleaned_data["user_email"]
                un = form.cleaned_data["user_name"]
                if un: 
                    if not User.objects.filter(username=un): 
                        u.username = un
                    else: 
                        # error - user exists
                        u.username = u.email
                else: 
                    u.username = u.email
                u.first_name = form.cleaned_data["firstname"]
                u.last_name = form.cleaned_data["surname"]
                u.save()
            if selected_choice.correct_choice: 
                # create or update access code
                code = Code.objects.filter(user=u).filter(code_type="rq0")
                # test of rq0 user group existence, if does not exist: create it
                try: 
                    g = Group.objects.get(name="rq0")
                except: 
                    g = Group()
                    g.name = "rq0"
                    g.save()
                # if user is not in "rq0" user group - add him
                if not u in g.user_set.all(): 
                    u.groups.add(g)
                if code: 
                    code = code[0]
                else: 
                    code = Code()
                    code.user = u
                    code.code_type = "rq0"
                code.created = datetime.datetime.now()
                code.valid_from = code.created
                code.valid_to = code.valid_from + datetime.timedelta(days=2)
                code.code_number = gen_code(5)
                code.save()

            return HttpResponse(str(form.cleaned_data))
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


