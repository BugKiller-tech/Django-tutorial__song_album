from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from music.models import Album, Song
# Create your views here.

def index(request):
  all_albums = Album.objects.all()
  res = ''
  for album in all_albums:
    res = res + album.artist
  context = {
    'all_albums': all_albums
  }
  return render(request, 'music/index.html', context)


def detail(request, album_id):
  # return HttpResponse(Song.objects.filter(id=album_id))
  # try:
  #   album = Album.objects.get(pk=album_id)
  #   return render(request, 'music/album_detail.html', {'album': album})
  # except Album.DoesNotExist:
  #   raise Http404("Sorry! Can not find the album")

  # instead of above we can do this easily
  album = get_object_or_404(Album, pk = album_id)
  return render(request, 'music/album_detail.html', {'album': album })
  
def favorite(request, album_id):
  album = get_object_or_404(Album, pk = album_id)
  try:
    selected_song = album.song_set.get(pk=request.POST['song'])
  except (KeyError, Song.DoesNotExist):
    return render(request, 'music/detail.html', {
      'album': album,
      'error_message': 'You did not select any valid song'
    })
  else:
    selected_song.is_favorite = True
    selected_song.save()
    return render(request, 'music/detail.html', {
      'album': album
    })
