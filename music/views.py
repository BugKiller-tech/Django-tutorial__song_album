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





class UserFormView(View):  # when we use View not the (CreateView, UpdateView, DeleteView),  then we can specify more detail info ourselves.
  form_class = UserForm
  template_name = 'music/registration_form.html'

  # display blank form
  def get(self, request):  # this is for the get request.
    form = self.form_class(None)
    return render(request, self.template_name, { 'form': form })
  
  # process form data here. post request!!
  def post(self, request):
    form = self.form_class(request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      
      # cleaned (normalized) data
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user.set_password(password) 
      user.save()

      # returns User objects if credentials are correct
      user = authenticate(username=username, password=password)

      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('music:index')
    return render(request, self.template_name, {'form': form})