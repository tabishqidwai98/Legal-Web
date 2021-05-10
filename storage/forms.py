from django import forms
from django.db.models import fields
from .models import Cases


class CasesUploadForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('Case_Name','description','category','Case_image')
