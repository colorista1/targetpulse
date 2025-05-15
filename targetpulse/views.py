from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

def index_view(request):
    return render(request, 'targetpulse/index.html')

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Попытка входа с email: {email}, пароль: {password}")  # Для отладки
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(f"Пользователь аутентифицирован: {user.username}")  # Для отладки
            login(request, user)
            next_url = request.GET.get('next', 'board_list')
            return redirect(next_url)
        else:
            print("Аутентификация не удалась.")  # Для отладки
            return render(request, 'targetpulse/login.html', {'error': 'Неверный email или пароль'})
    return render(request, 'targetpulse/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return render(request, 'targetpulse/register.html', {'error': 'Пароли не совпадают'})

        if User.objects.filter(email=email).exists():
            return render(request, 'targetpulse/register.html', {'error': 'Пользователь с таким email уже существует'})

        if User.objects.filter(username=username).exists():
            return render(request, 'targetpulse/register.html', {'error': 'Пользователь с таким именем уже существует'})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('board_list')
        else:
            return render(request, 'targetpulse/register.html', {'error': 'Не удалось войти после регистрации'})

    return render(request, 'targetpulse/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    return render(request, 'targetpulse/admin_page.html', {'message': 'Добро пожаловать, администратор!'})