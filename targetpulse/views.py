from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Task, UserProfile
from django import forms

# Форма для редактирования профиля
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

def index_view(request):
    return render(request, 'targetpulse/index.html')

def task_detail(request, pk):
    return render(request, 'targetpulse/task_detail.html', {'task': {'title': 'Тестовая задача'}})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Попытка входа с email: {email}, пароль: {password}")  # Для отладки
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(f"Пользователь аутентифицирован: {user.username}")  # Для отладки
            login(request, user)
            next_url = request.GET.get('next', 'index')  # Изменено на index
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

        # Создаём UserProfile для нового пользователя
        UserProfile.objects.create(user=user)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Изменено на index
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

@login_required
def profile_view(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            if 'email' in request.POST and request.POST['email']:
                request.user.email = request.POST['email']
                request.user.save()
            # Проверяем и обновляем никнейм
            if 'username' in request.POST and request.POST['username']:
                if User.objects.filter(username=request.POST['username']).exclude(id=request.user.id).exists():
                    return render(request, 'targetpulse/profile.html', {
                        'user': request.user,
                        'profile_form': profile_form,
                        'error': 'Этот никнейм уже занят'
                    })
                request.user.username = request.POST['username']
                request.user.save()
            # Проверяем и обновляем пароль
            if 'password' in request.POST and request.POST['password']:
                request.user.set_password(request.POST['password'])
                request.user.save()
                login(request, request.user)
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=user_profile)
    
    return render(request, 'targetpulse/profile.html', {
        'user': request.user,
        'profile_form': profile_form
    })
    
@login_required
def board_list(request):
    return render(request, 'targetpulse/board_list.html', {})