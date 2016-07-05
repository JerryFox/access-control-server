from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Code

class IndexView(generic.ListView):
    template_name = 'accesscodes/index.html'
    context_object_name = 'code_list'

    def get_queryset(self):
        """
        """
        return Code.objects.all() 


