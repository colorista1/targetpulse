from django.urls import path
from targetpulse import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/create/', views.board_create, name='board_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/<int:board_id>/', views.task_create, name='task_create'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('boards/', views.board_list, name='board_list'),
]