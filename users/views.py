from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm, lawyerProfileForm, UserProfileForm, CasesFoughtForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Category, lawyer_Profile, Cases_Fought, User_Profile

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

            return redirect(to='view_lawyer')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'addProfileForm':filled_form}
            return render (request,'users/add_lawyer.html',ctx)

class lawyerProfileListView(ListView):
    model = lawyer_Profile
    template_name = "users/view_lawyer.html"
    paginate_by = 8
    

def query_Lawyer_Profile(request):
    query = request.GET.get('q','')
   
    results = lawyer_Profile.objects.filter(name__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'users/search_lawyer.html',context)

def detail_of_lawyer(request,pk):
    result = lawyer_Profile.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'users/detail_lawyer.html',context)

def edit_lawyer_profile(request,id):
    context = {}
    return render(request,'users/edit_lawyer.html',context)

def User_Profile(request):
    if request.method == 'GET':
        form = UserProfileForm()
        return render(request,'users/add_User.html',{'addUserform':form})
    elif request.method == 'POST':
        filled_form = UserProfileForm(request.POST, request.FILE)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'Profile saved successfully')

            return redirect(to='view_user')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'addUserForm':filled_form}
            return render (request,'users/add_User.html',ctx)

def Cases_Fought_view(request):
    if request.method == 'GET':
        form = CasesFoughtForm()
        return render(request,'users/add_casesFought.html',{'casesFoughtForm':form})
    elif request.method == 'POST':
        filled_form = CasesFoughtForm(request.POST, request.FILE)
        if filled_form.is_valid():
            filled_form.save()

            messages.add_message(request, messages.SUCCESS, 'details saved successfully')

            return redirect(to='add_casesFought')
        else:
            messages.add_message(request, messages.ERROR, 'Form details are invalid, please check')
            ctx = {'casesFoughtForm':filled_form}
            return render (request,'users/add_casesFought.html',ctx)