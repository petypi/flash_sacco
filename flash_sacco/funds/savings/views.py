from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse
# Create your views here.


class SavingsRedirect(TemplateView):
    template_name = 'savings/index.html'

    def get_context_data(self, **kwargs):
        context=super(SavingsRedirect, self).get_context_data(**kwargs)
        context["title"]="This is a useless page"
        return context

