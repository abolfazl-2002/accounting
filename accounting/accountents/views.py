from django.shortcuts import render
from .models import AccountryTable # models
from django.views.generic import (
    CreateView,ListView,DeleteView,UpdateView,DetailView
    )
from django.urls import reverse

# Create your views here.

class Accountents_HomePage_View(ListView):
    model = AccountryTable
    template_name = ""
    context_object_name = "object"

class Accountents_InfoPage_View(DetailView):
    model = AccountryTable
    template_name = ""
    context_object_name = "object"

class AddPageView(CreateView):
    model = AccountryTable
    template_name = ""
    fields = ["title","description","price","group"]

class Accountents_EditPage_View(UpdateView):
    model = AccountryTable
    template_name = ""
    fields = ["title","description","price","group"]

class Accountents_DeletPage_View(DeleteView):
    model = AccountryTable
    template_name = ""
    success_url = reverse()