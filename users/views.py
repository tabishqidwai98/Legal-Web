from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm, lawyerProfileForm, User_Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def register(request):
    if request.method == 'GET': # agar page open kia aapne
        return render(request, 'users/register.html',{'form':CustomUserCreationForm})
    elif request.method == 'POST': # agar form submit kra to
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)      
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()             # save the user detail in database
            login(request, user)    # let the autologin work
            return redirect(reverse('dashboard'))      # redirect to dashboard pasword
        else:
            return render(request, 'users/register.html',{'form':CustomUserCreationForm})

@login_required
def lawyer_Profile(request):
    if request.method == 'GET':
        form = lawyerProfileForm()
        return render(request,'users/add_lawyer.html',{'addProfileform':form})
    elif request.method == 'POST':
        filled_form = lawyerProfileForm(request.POST, request.FILE)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile saved successfully')

            return redirect(to='add_lawyer')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'addProfileForm':filled_form}
            return render (request,'users/add_lawyer.html',ctx)

def User_Profile(request):
    context = {}
    return render(request,'users/add_User.html',context)