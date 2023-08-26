from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture', 'caption', 'album', 'is_private']


class PictureDeleteForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['caption']

    def clean_title(self):
        title = self.cleaned_data['caption']
        if self.instance.title != title:
            raise ValidationError('Название не совпадает')
        return title