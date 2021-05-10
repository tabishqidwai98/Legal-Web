from django.shortcuts import render, redirect
from .models import AiModel
from .forms import AiModelUploadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.
@login_required
def upload_form(request):
    
    if request.method=='POST':
        # after form is submitte
        filled_form = AiModelUploadForm(request.POST,request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            # save a message in message system
            messages.add_message(request, messages.SUCCESS, 'AI Model details uploaded successfully')
            # redirect to new page
            return redirect(to='view_model')

        else:
            # if form has errors
            # # save a message in message system
            messages.add_message(request, messages.ERROR, 'form details are invalid, please check')
            ctx = {'uploadform':filled_form}
            return render(request,'storage/add.html',ctx)

    if request.method =='GET':
        # BLANK FORM
        form = AiModelUploadForm()
        
    return render(request,'storage/add_ai_model.html',{'uploadform':form})


class AiModelListView(ListView):
    model = AiModel
    template_name = "storage/view.html"
    paginate_by = 10
    

def query_ai_models(request):
    query = request.GET.get('q','')
   
    results = AiModel.objects.filter(name__contains=query)
    paginator = Paginator(results, 2) # num of result to show per page, change this
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'result':page_obj,
        'query':query
    }
    
    return render(request,'storage/search.html',context)

def detail_of_ai_model(request,pk):
    result = AiModel.objects.get(pk=pk)
    context = {'result':result}
    return render(request,'storage/detail.html',context)

def edit_ai_model(request,id):
    context = {}
    return render(request,'storage/edit.html',context)