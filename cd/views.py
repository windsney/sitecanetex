from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView, FormView

# Create your views here.
class Home(TemplateView):
    template_name = "index.html"
