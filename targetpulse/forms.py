from django import forms
from .models import Board, Task

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description', 'is_public']
        labels = {
            'title': 'Название доски',
            'description': 'Описание',
            'is_public': 'Публичная доска',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название доски'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'rows': 4}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'deadline', 'progress']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'status': 'Статус',
            'priority': 'Приоритет',
            'deadline': 'Дедлайн',
            'progress': 'Прогресс выполнения (%)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название задачи'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'progress': forms.NumberInput(attrs={'class': 'form-range', 'type': 'range', 'min': 0, 'max': 100, 'step': 1, 'oninput': 'progressOutput.value = value'}),
        } 