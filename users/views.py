from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm,ProfileForm, CasesFoughtForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Category,Profile, Cases_Fought


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
     return render(request, 'contact.html')

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
def lawyer_Profile_views(request):
    if request.method == 'GET':
        form = ProfileForm()
        return render(request,'users/add_lawyer.html',{'addProfileform':form})
    elif request.method == 'POST':
        filled_form = ProfileForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile saved successfully')

            return redirect(to='view_lawyer')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'addProfileForm':filled_form}
            return render (request,'users/add_lawyer.html',ctx)

class lawyerProfileListView(ListView):
    model = Profile
    template_name = "users/view_lawyer.html"
    paginate_by = 8
    

def query_Lawyer_Profile(request):
    query = request.GET.get('q','')
   
    results = Profile.objects.filter(Name__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_lawyer.html',context)

def detail_of_lawyer(request,pk):
    result = Profile.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_lawyer.html',context)

def edit_lawyer_profile(request,id):
    context = {}
    return render(request,'users/edit_lawyer.html',context)

@login_required
def User_Profile_view(request):
    if request.method == 'GET':
        form = ProfileForm()
        return render(request,'users/add_User.html',{'addUserform':form})
    elif request.method == 'POST':
        filled_form = ProfileForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile saved successfully')

            return redirect(to='view_Users')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'addUserForm':filled_form}
            return render (request,'users/add_User.html',ctx)

class UserProfileListView(ListView):
    model = Profile
    template_name = "users/view_User.html"
    paginate_by = 8
    

def query_User_Profile(request):
    query = request.GET.get('q','')
   
    results = Profile.objects.filter(Username__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_User.html',context)

def detail_of_User(request,pk):
    result = Profile.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_User.html',context)

def your_User_Profile(request,pk):
    result = Profile.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/view_lawyer_profile.html',context)

def edit_User_Profile(request,id):
    context = {}
    return render(request,'users/edit_User.html',context)

@login_required
def Cases_Fought_view(request):
    if request.method == 'GET':
        form = CasesFoughtForm()
        return render(request,'users/add_casesFought.html',{'casesFoughtForm':form})
    elif request.method == 'POST':
        filled_form = CasesFoughtForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'details saved successfully')

            return redirect(to='view_fought')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'casesFoughtForm':filled_form}
            return render (request,'users/add_casesFought.html',ctx)

class CasesFoughtListView(ListView):
    model = Cases_Fought
    template_name = "users/view_casesFought.html"
    paginate_by = 8
    

def query_Cases_Fought(request):
    query = request.GET.get('q','')
   
    results = Cases_Fought.objects.filter(Cases__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_casesFought.html',context)

def detail_of_Cases_Fought(request,pk):
    result = Cases_Fought.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_casesFought.html',context)

def edit_Cases_Fought(request,id):
    context = {}
    return render(request,'users/edit_casesFought.html',context)


