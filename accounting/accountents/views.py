from django.shortcuts import render
from .models import AccountryTable # models
from django.views.generic import (
    CreateView,ListView,DeleteView,UpdateView,DetailView
    )
from django.urls import reverse

# Create your views here.
url = "accountents/"
class Accountents_HomePage_View(ListView):
    model = AccountryTable
    template_name = url + "home.html"
    context_object_name = "object"

class Accountents_InfoPage_View(DetailView):
    model = AccountryTable
    template_name = url + "detail.html"
    context_object_name = "object"

class Accountents_AddPage_View(CreateView):
    model = AccountryTable
    template_name = url + "new.html"
    fields = ["title","description","price","group"]

class Accountents_EditPage_View(UpdateView):
    model = AccountryTable
    template_name = url + "edit.html"
    fields = ["title","description","price","group"]

class Accountents_DeletPage_View(DeleteView):
    model = AccountryTable
    template_name = url + "delete.html"
    success_url = reverse()