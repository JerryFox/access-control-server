from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q

from .models import Code

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

