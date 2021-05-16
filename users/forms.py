from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import Cases_Fought, Category,lawyer_Profile,User_Profile  

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class lawyerProfileForm(forms.ModelForm):
    class Meta:
        model = lawyer_Profile
        fields = ('Name','Email','Phone_No','Category','Profile_Photo','Gender','General_Fee')
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('Username','email','contact_no','address','image','bio')

class CasesFoughtForm(forms.ModelForm):
    class Meta:
        model = Cases_Fought
        fields = ('Cases','Summary','category','Email')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ('Name','Email','Category')