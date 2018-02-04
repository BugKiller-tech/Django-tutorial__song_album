from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


from .models import Album, Song
from .forms import UserForm


class IndexView(generic.ListView):
  template_name = 'music/index.html'
  context_object_name = 'all_albums'  # this is 'object_list' as default. we can use this name as variable name in the template file.
  def get_queryset(self): # This is for get the data for index page. name is predefined keyword, that means you can not make this function name yourself.
    return Album.objects.all()


class DetailView(generic.DetailView):
  template_name = 'music/album_detail.html'
  model = Album






class AlbumCreate(CreateView):
  model = Album
  fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
  model = Album
  fields = ['artist', 'album_title', 'genre', 'album_logo']



class AlbumDelete(DeleteView):
  model = Album
  success_url = reverse_lazy('music:index')