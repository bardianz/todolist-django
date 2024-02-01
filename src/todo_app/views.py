from urllib import request
from django.shortcuts import redirect, render, get_object_or_404
from todo_app.models import ToDoItem
from django.contrib.auth.decorators import login_required
from todo_app.forms import ToDoItemAddForm, ToDoItemEditForm
from django.http import HttpResponseForbidden

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return redirect('account/dashboard')
    context = {
        'title': "To Do List",
    }
    return render(request, 'todo_app/home.html', context)
    
# @login_required(login_url='/account/login')
# def dashboard_view(request):
#     user = request.user
#     query = ToDoItem.objects.filter(owner=user)
#     number_of_items = len(query)
#     print(number_of_items)
#     context = {
#         'number_of_items': number_of_items,
#     }

#     return render(request, 'todo_app/dashboard.html', context)


@login_required(login_url='/account/login')
def items_list_view(request):
    user = request.user
    query = ToDoItem.objects.filter(owner=user).order_by('-created_date')
    context = {
        'todo_items_list': query,
        'items_len': len(query),
    }
    return render(request, 'todo_app/tasks_list.html', context)


@login_required(login_url='/account/login')
def create_new_task(request):
    user = request.user
    if request.method == 'POST':
        form = ToDoItemAddForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            return redirect('todo_app:tasks_list')
    form = ToDoItemAddForm()
    return render(request, 'todo_app/create_new_task.html', {'form': form})


@login_required(login_url='/account/login')
def delete_task(request, id):
    try:
        item = ToDoItem.objects.get(id=id)
    except:
        return redirect("todo_app:tasks_list")
    if item.owner == request.user:
        item.delete()
        return redirect("todo_app:tasks_list")
    else:
        return redirect("todo_app:tasks_list")


@login_required(login_url='/account/login')
def edit_task_view(request, id):
    context = {}
    if request.method == 'POST':
        item = ToDoItem.objects.get(pk=id)
        context += {'item': item}
        form = ToDoItemEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_app:tasks_list')
    form = ToDoItemAddForm()
    context = {
        'form': form,
    }

    return render(request, 'todo_app/edit_task.html', context)


@login_required(login_url='/account/login')
def task_detail_view(request, id):
    if request.method == 'POST':
        item = ToDoItem.objects.get(pk=id)
        form = ToDoItemEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_app:tasks_list')

    try:
        task = ToDoItem.objects.get(pk=id)
        context = {
            'task': task,
        }
        return render(request, 'todo_app/task_detail.html', context)
    except:
        return render(request, 'todo_app/task_detail.html')


def about_us_view(request):
    return render(request, 'todo_app/about_us.html')