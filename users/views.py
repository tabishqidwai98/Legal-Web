from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CasesFoughtForm, LawyerForm, ClientForm, ClientSignUpForm, LawyerSignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator
from .models import Category, Cases_Fought,User,Lawyer, Client


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
    return render(request, 'users/register.html')

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('dashboard')

class LawyerSignUpView(CreateView):
    model = User
    form_class = LawyerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'lawyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('dashboard') 

def lawyer_Profile(request):
    if request.method == "POST":
        user_form = LawyerForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))
        else:
            messages.error(request,('Unable to complete request'))
        return redirect ("profile")
    user_form = LawyerForm()
    return render(request = request, template_name ="users/profile.html", context = {"user":request.user, 
        "user_form": user_form})

def lawyer_Profile_views(request, pk):
    result = Lawyer.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_lawyer.html',context)

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
    model = Lawyer
    template_name = "users/view_lawyer.html"
    paginate_by = 8
    

def query_Lawyer_Profile(request):
    query = request.GET.get('q','')
   
    results = Lawyer.objects.filter(user__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_lawyer.html',context)

def detail_of_lawyer(request,pk):
    result = Lawyer.objects.get(pk=pk)
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
    model = Client
    template_name = "users/view_User.html"
    paginate_by = 8
    

def query_User_Profile(request):
    query = request.GET.get('q','')
   
    results = Client.objects.filter(Username__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_User.html',context)

def detail_of_User(request,pk):
    result = Client.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_User.html',context)

def your_User_Profile(request,pk):
    result = Client.objects.get(pk=pk)
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