from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Picture, Favorite, Album


class PhotoFavoriteAPIView(LoginRequiredMixin, APIView):
    def post(self, request, pk, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=pk)
        user = request.user
        favorite, created = Favorite.objects.get_or_create(user=user, picture=picture)
        if not created:
            favorite.delete()
        return Response(status=status.HTTP_200_OK)


class AlbumFavoriteAPIView(LoginRequiredMixin, APIView):
    def post(self, request, pk, *args, **kwargs):
        album = get_object_or_404(Album, pk=pk)
        user = request.user
        favorite, created = Favorite.objects.get_or_create(user=user, album=album)
        if not created:
            favorite.delete()
        return Response(status=status.HTTP_200_OK)