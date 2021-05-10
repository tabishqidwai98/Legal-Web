from django import forms
from django.db.models import fields
from .models import AiModel


class AiModelUploadForm(forms.ModelForm):
    class Meta:
        model = AiModel
        fields = ('name','summary','category','model_file','model_image')
