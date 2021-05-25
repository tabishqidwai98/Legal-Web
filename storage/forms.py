from django import forms
from django.db.models import fields
from .models import Cases


class CasesUploadForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('caseName','description','category','case_image','contact_No')
