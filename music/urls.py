from django.urls import path, include
from . import views as musicViews
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'music' # this is really good to seperate many apps. when you specify this, then url tag will be music:route_name

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('register/', views.UserFormView.as_view(), name='register'),


  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
  path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
  path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]


# urlpatterns = [
#   path('', musicViews.index, name='index'),
#   path('<int:album_id>/', musicViews.detail, name='detail'),
#   path('<int:album_id>/favorite/', musicViews.favorite, name='favorite')
# ]

# if settings.DEBUG:
#   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
