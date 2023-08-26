from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm, AlbumDeleteForm
from webapp.models import Album, Picture


class AlbumDetailView(LoginRequiredMixin,DetailView):
    model = Album
    template_name = 'album/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pictures = Picture.objects.filter(album=self.object, album__is_private=False)
        context['pictures'] = pictures
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'album/album_create.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/album_update.html'
    context_object_name = 'album'
    permission_required = 'webapp.album_change'

    def has_permission(self):
        def has_permission(self):
            return super().has_permission() or self.get_object().author == self.request.user

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Picture
    template_name = 'album/album_delete.html'
    context_object_name = 'picture'
    success_url = reverse_lazy('webapp:index')
    form_class = AlbumDeleteForm
    permission_required = 'webapp.delete_album'

    def has_permission(self):
        def has_permission(self):
            return super().has_permission() or self.get_object().author == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)