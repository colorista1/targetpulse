from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/create/', views.board_create, name='board_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('board/<int:board_id>/task/create/', views.task_create, name='task_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
