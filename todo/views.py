from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from datetime import datetime

# Create your views here.
from .models import Todo
from .forms import TodoForm

def todo(request):
    todos = None

    if request.user.is_authenticated:
        todos = Todo.objects.filter(user = request.user)

    return render(request, 'todo/todo.html', {'todos': todos})

@login_required
def view_todo(request, id):
    msg = ''
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo) # instance=todo: 將 todo 資料先行填入 form 
    date = todo.created.strftime('%Y-%m-%d %H:%M:%S')
    
    if request.method == 'POST':
        if request.POST.get('delete'):
            todo.delete()

            return redirect('todo')

        elif request.POST.get('update'):
            try:
                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    todo = form.save(commit=False)
                    
                    todo.date_completed = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if todo.completed else None

                    todo.save()


                    return redirect('todo')
            except Exception as e:
                print(e)
                msg = '更新失敗!!!'

    return render(request, 'todo/view.html', {'todo': todo, 'date': date, 'form': form, 'msg':msg})

@login_required
def create_todo(request):
    msg = ''
    form = TodoForm()

    if request.method == 'POST':
        try:
            form = TodoForm(request.POST)
            if form.is_valid(): # 檢查是否符合規定
                todo = form.save(commit=False) # commit=False: 先不儲存: 暫存
                todo.user = request.user
                todo.save()

                return redirect('todo')
        except Exception as e:
            msg = '資料有誤!!!'
            print(e)

    return render(request, 'todo/create.html', {'form':form, 'msg':msg})

@login_required
def complete_todo(request):
    todos = Todo.objects.filter(user=request.user, completed=True)

    return render(request, 'todo/completed.html', {'todos':todos})

@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()

    return redirect('todo')
    