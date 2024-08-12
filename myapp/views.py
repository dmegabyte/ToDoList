from django.shortcuts import render,redirect, get_object_or_404
from .models import User, Todo
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password

from .forms import TodoForm

def index(request):
    if request.method == 'POST':
        print(request.POST)
        todo_form = TodoForm(request.POST)
        
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.save()


            messages.add_message(request, messages.INFO, 'Задача успешно добавлена!')
            return redirect('home')
    
    context = {'todoform':TodoForm()     }

    # print(TodoForm())


    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user).order_by('-created_at')
        context['todos'] = todos

    return render(request, 'myapp/index.html', context=context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            username = username.lower()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.add_message(request, messages.INFO, 'НЕПРАВИЛЬНОЕ ИМЯ ПОЛЬЗОВАТЕЛЯ ИЛИ ПАРОЛЬ')
                return redirect('login')
        except:
            messages.add_message(request, messages.INFO, 'ОШИБКА!')
            return redirect('login')
    return render(request, 'myapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            username = username.lower()
            password = make_password(password)
            user = User(username=username,password=password)           
            user.save()
            return redirect('login')
        except:
            messages.add_message(request, messages.INFO, 'ОШИБКА!')
            return redirect('register')

    return render(request, 'myapp/register.html')

# Create your views here.

def delete_func(request, id):
    
    todo =  get_object_or_404(Todo, id=id)
    if request.user == todo.user:
        todo.delete()
    return redirect('home')


def toggle(request, id):
    todo = get_object_or_404(Todo, id=id)
    if todo.user == request.user:
        todo.completed = not todo.completed
        todo.save()
    return redirect('home')
