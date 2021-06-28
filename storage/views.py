from users.models import Client
from django.shortcuts import render, redirect, HttpResponse
from .models import Cases, ReviewCases
from .forms import CasesUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator
import mimetypes
import os

# Create your views here.
@login_required
def upload_form(request):
    
    if request.method=='POST':
        # after form is submitted
        filled_form = CasesUploadForm(request.POST,request.FILES)
        if filled_form.is_valid():
            #filled_form.save()
            form_data = filled_form.save(commit=False)
            userid = request.user.id
            client = Client.objects.get(pk=userid)
            form_data.user = client
            form_data.save()
            # save a message in message system
            messages.add_message(request, messages.SUCCESS, 'Case details uploaded successfully')
            # redirect to new page
            return redirect(to='view_cases')

        else:
            # if form has errors
            # # save a message in message system
            messages.add_message(request, messages.ERROR, 'form details are invalid, please check')
            ctx = {'uploadform':filled_form}
            return render(request,'storage/add.html',ctx)

    #if request.method =='GET':
        # BLANK FORM
    form = CasesUploadForm()
    ctx = {'uploadform':form}
    return render(request,'storage/add.html',ctx)


# @login_required
# def case_view(request):
#     client = Client.objects.get(user=request.user)
#     print("client",client)
#     results = Cases.objects.filter(user=client)
#     print("results",results)
#     paginator = Paginator(results, 6) # num of result to show per page, change this
#     page_num = request.GET.get('page')
#     page_obj = paginator.get_page(page_num)
#     context = {
#         'page_obj':page_obj,
#     }
#     return render(request,'storage/view.html',context)

@login_required
def case_view(request):
    # client = Client.objects.get(user=request.user)
    # print("client",client)
    # results = Cases.objects.filter(user=client)
    # print("results",results)
    results = Cases.objects.all()
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'page_obj':page_obj,
    }
    return render(request,'storage/view.html',context)

def query_Cases(request):
    query = request.GET.get('q','')
   
    results = Cases.objects.filter(caseName__contains=query)
    paginator = Paginator(results, 6) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'storage/search.html',context)

def detail_of_Cases(request,pk):
    result = Cases.objects.get(pk=pk)
    reviews = ReviewCases.objects.filter(Case_id=pk)
    ctx = {'result':result,'reviews':reviews}
    return render(request,'storage/detail.html',ctx)

def edit_Case(request,pk):
    try:
        data = Cases.objects.get(pk=pk)
        if request.method == 'POST':
            form = CasesUploadForm(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return redirect(to='view_cases')
        else:
            form = CasesUploadForm(instance=data)
        context = {'cform': form}
        return render(request,'storage/edit.html',context)
    except Exception as e:
        print('some error occurred')
        return redirect(to='view_cases')

def delete_case(request,pk):
    try:
        Cases.objects.filter(pk=pk).delete()
    except:
        print('some error occurred')

    return redirect(to='view_cases')