from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures/', null=False, blank=False)
    caption = models.CharField(max_length=255, null=False, blank=False, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False,
                               verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name='Альбом')
    is_private = models.BooleanField(default=False, verbose_name='Статус')

    def get_absolute_url(self):
        return reverse('webapp:picture_detail', kwargs={'pk': self.pk})


class Album(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название альбома')
    desctiption = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Описание альбома')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_private = models.BooleanField(default=False, verbose_name='Статус')

    def get_absolute_url(self):
        return reverse('webapp:album_detail', kwargs={'pk': self.pk})


class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False)
    picture = models.ForeignKey('webapp.Picture', on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, null=True, blank=True)
