from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from django.contrib.auth.models import User
from .models import Cases_Fought, Category, Lawyer, Client,Rating
from django.db import transaction
from django.forms.widgets import RadioSelect
from django_starfield import Stars

from .models import Client, User,Lawyer 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ('designation','contact','email','pic','gender','city','lawyertype','experience')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('gender','contact','email','pic')

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
    image  = forms.ImageField()
    contact = forms.CharField(max_length=15,widget=forms.TextInput)
    class Meta(UserCreationForm.Meta):
        model= User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.gender = self.cleaned_data.get('gender')
        client.contact = self.cleaned_data.get('contact') 
        client.email = self.cleaned_data.get('email') 
        client.pic = self.cleaned_data.get('image') 
        client.save()
        return user

class LawyerSignUpForm(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput)
    designation = forms.CharField(widget=forms.TextInput)
    gender = forms.ChoiceField(choices=Lawyer.GENDER_CHOICE, widget=forms.RadioSelect)
    lawyertype = forms.CharField(widget=forms.TextInput)
    experience = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)
    image  = forms.ImageField()
    contact = forms.CharField(max_length=15,widget=forms.TextInput)
    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_lawyer = True
        user.save()
        lawyer = Lawyer.objects.create(user=user)
        lawyer.gender = self.cleaned_data.get('gender')
        lawyer.designation = self.cleaned_data.get('designation')
        lawyer.lawyertype = self.cleaned_data.get('lawyertype')
        lawyer.experience = self.cleaned_data.get('experience')
        lawyer.city = self.cleaned_data.get('city') 
        lawyer.contact = self.cleaned_data.get('contact') 
        lawyer.pic = self.cleaned_data.get('image') 
        lawyer.email = self.cleaned_data.get('email') 
        lawyer.save()
        return user

class RatingForm(forms.ModelForm):
    """Form definition for Rating."""

    class Meta:
        """Meta definition for Ratingform."""

        model = Rating
        fields = ('score',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'] = forms.FloatField(max_value=5, min_value=0)
       
