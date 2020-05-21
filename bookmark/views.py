from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from bookmark.models import Bookmark


class BookmarkList(ListView):  # bookmark_lsit.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark_form.html
    model = Bookmark
    fields = ['site_name', 'url']   # <form>가 들어가는 것은 files를 넣어줌
    template_name_suffix = '_create'  # bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark
