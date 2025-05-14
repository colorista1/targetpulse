from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_boards')
    members = models.ManyToManyField(User, related_name='boards')

    def __str__(self):
        return self.title

class Task(models.Model):
    STATUSES = [('В ожидании', 'В ожидании'), ('В работе', 'В работе'), ('Завершено', 'Завершено')]
    PRIORITIES = [('Низкий', 'Низкий'), ('Средний', 'Средний'), ('Высокий', 'Высокий')]
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUSES, default='В ожидании')
    priority = models.CharField(max_length=50, choices=PRIORITIES, default='Средний')
    deadline = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    progress = models.IntegerField(default=0)
    total_time = models.FloatField(default=0.0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return self.title

class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_spent = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} - {self.time_spent} часов"