from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def board_list(request):
    return render(request, 'targetpulse/board_list.html', {'boards': []})

def board_detail(request, pk):
    return render(request, 'targetpulse/board_detail.html', {'board': {'title': 'Тестовая доска', 'tasks': []}, 'statuses': ['В ожидании', 'В работе', 'Завершено']})

def board_create(request):
    return render(request, 'targetpulse/board_create.html')

def task_detail(request, pk):
    return render(request, 'targetpulse/task_detail.html', {'task': {'title': 'Тестовая задача'}})

def task_create(request, board_id):
    return render(request, 'targetpulse/task_create.html', {'board': {'id': board_id}})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'board_list')  # Используем имя маршрута
            return redirect(next_url)
        else:
            return render(request, 'targetpulse/login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'targetpulse/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')