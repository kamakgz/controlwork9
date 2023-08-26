from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm

from webapp.models import Picture, Album, Favorite


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url

        return reverse('webapp:index')

class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user_obj']
        user_obj_pictures = Picture.objects.filter(author=user).exclude(is_private=True)
        user_obj_albums = Album.objects.filter(author=user).exclude(is_private=True)
        user_obj_favorites = Favorite.objects.filter(user=user)
        if user == self.request.user:
            private_albums = Album.objects.filter(author=user, is_private=True)
            private_pictures = Picture.objects.filter(author=user, is_private=True)
            context['private_albums'] = private_albums
            context['private_pictures'] = private_pictures
        context['user_obj_pictures'] = user_obj_pictures
        context['user_obj_albums'] = user_obj_albums
        context['user_obj_favorites'] = user_obj_favorites
        return context
