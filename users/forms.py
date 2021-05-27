from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from .models import Cases_Fought, Category, Lawyer, Client
from django.db import transaction
from django.forms.widgets import RadioSelect

from .models import Client, User,Lawyer 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ('designation','gender','city','lawyertype','experience')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('gender',)

class CasesFoughtForm(forms.ModelForm):
    class Meta:
        model = Cases_Fought
        fields = ('case','summary','category','status')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ('category',)

class ClientSignUpForm(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput)
    gender = forms.ChoiceField(choices=Client.GENDER_CHOICE, widget=forms.RadioSelect)
    class Meta(UserCreationForm.Meta):
        model= User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.gender = self.cleaned_data.get('gender')

class LawyerSignUpForm(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput)
    designation = forms.CharField(widget=forms.TextInput)
    gender = forms.ChoiceField(choices=Lawyer.GENDER_CHOICE, widget=forms.RadioSelect)
    lawyertype = forms.CharField(widget=forms.TextInput)
    experience = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)
    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lawyer = True
        user.save()
        laywer = Lawyer.objects.create(user=user)
        laywer.gender = self.cleaned_data.get('gender')
        laywer.designation = self.cleaned_data.get('designation')
        laywer.lawyertype = self.cleaned_data.get('lawyertype')
        laywer.experience = self.cleaned_data.get('experience')
        laywer.city = self.cleaned_data.get('city') 