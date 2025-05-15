from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('boards/', views.board_list, name='board_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('profile/', views.profile_view, name='profile'),
]