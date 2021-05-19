from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import Cases_Fought, Category,Profile  

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','contact_no','address','image','gender','bio','user_type')

class CasesFoughtForm(forms.ModelForm):
    class Meta:
        model = Cases_Fought
        fields = ('case','summary','category','user','status')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ('category',)