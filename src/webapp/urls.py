from django.urls import path
from webapp.views import IndexView, PictureDetailView, PictureCreateView, PictureUpdateView, PictureDeleteView, \
    AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='picture_detail'),
    path('picture/create/', PictureCreateView.as_view(), name='picture_create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture_update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete')
]