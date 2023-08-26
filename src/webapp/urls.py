from django.urls import path
from webapp.views import IndexView, PictureDetailView, PictureCreateView, PictureUpdateView, PictureDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='picture_detail'),
    path('picture/create/', PictureCreateView.as_view(), name='picture_create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture_update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete')
]