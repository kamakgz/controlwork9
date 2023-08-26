from django.urls import path
from api.views import PhotoFavoriteAPIView, AlbumFavoriteAPIView

app_name = 'api'

urlpatterns = [
    path('picture/<int:pk>/favorite/', PhotoFavoriteAPIView.as_view(), name='photo_favorite'),
    path('album/<int:pk>/favorite/', AlbumFavoriteAPIView.as_view(), name='album_favorite')
]