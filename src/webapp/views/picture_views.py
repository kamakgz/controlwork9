from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PictureForm, PictureDeleteForm
from webapp.models import Picture


class IndexView(ListView):
    model = Picture
    template_name = 'picture/index.html'
    context_object_name = 'pictures'
    ordering = '-created_at'
    paginate_by = 5

    def get_queryset(self):
        return Picture.objects.filter(is_private=False)


class PictureDetailView(DetailView):
    model = Picture
    template_name = 'picture/detail.html'
    context_object_name = 'picture'


class PictureCreateView(LoginRequiredMixin, CreateView):
    template_name = 'picture/create.html'
    form_class = PictureForm
    model = Picture

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PictureUpdateView(UpdateView):
    model = Picture
    template_name = 'picture/update.html'
    form_class = PictureForm
    context_object_name = 'picture'

class PictureDeleteView(DeleteView):
    model = Picture
    template_name = 'picture/delete.html'
    context_object_name = 'picture'
    success_url = reverse_lazy('webapp:index')
    form_class = PictureDeleteForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)