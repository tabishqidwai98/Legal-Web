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
            form_data.Name = request.user
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


class CasesListView(ListView):
    model = Cases
    template_name = "storage/view.html"
    paginate_by = 8
    

def query_Cases(request):
    query = request.GET.get('q','')
   
    results = Cases.objects.filter(CaseName__contains=query)
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
    context = {'result':result,'reviews':reviews}
    return render(request,'storage/detail.html',context)

def edit_Cases(request,id):
    result = Cases.objects.get(pk=id)
    context = {'result':result}
    return render(request,'storage/edit.html',context)