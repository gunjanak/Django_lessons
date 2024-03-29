from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "post_detail.html"



class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","body"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    

    