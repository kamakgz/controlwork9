from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Picture, Album


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'caption', 'album', 'is_private']


class PictureDeleteForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['caption']

    def clean_title(self):
        caption = self.cleaned_data['caption']
        if self.instance.caption != caption:
            raise ValidationError('Название не совпадает')
        return caption


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'desctiption', 'is_private']


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title']

    def clean_title(self):
        title = self.cleaned_data['title']
        if self.instance.title != title:
            raise ValidationError('Название не совпадает')
        return title