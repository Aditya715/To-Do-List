"""
    Although if we want we can do the changes in the front end without refreshing the page.
    But as nothing mentioned over their and I didn't have the designs and I'm not aware that 
    how many changes it'll take that's why skipping coding of jquery.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Task
from .forms import AddTaskForm


# Create your views here.
@login_required
def dashboard(request):
    """
        Dashboard views.
    """
    context = {
        'queryset': Task.objects.all()
    }
    return render(request, 'task_list/index.html', context)

@login_required
def add_new(request):
    """
        Add new task views.
    """
    form = AddTaskForm(request.POST or None)
    # check if form is valid or not.
    if form.is_valid():
        form.save()
        return redirect('task_list:dashboard')
    
    return render(request, 'task_list/add.html', {'form': form})

# ajax hit to mark down complete
def mark_me_complete(request):
    """
        This function is called by the ajax hit to bring changes in the models that task
        has been completed. Model Update is the basic thing it wants to do.
    """
    query_id = request.POST.get('id')
    query_id = query_id.replace("query", "")
    query_obj = Task.objects.filter(pk=query_id)
    query_obj.update(status='completed')
    return JsonResponse({"status" : True})