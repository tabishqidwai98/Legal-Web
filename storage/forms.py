from django import forms
from django.db.models import fields
from .models import Cases


class CasesUploadForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('Case_Name','Description','Category','Case_image','Name','Contact_No',)
