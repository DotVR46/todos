from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:category_id>/', views.todo_list, name='todo_list_by_category'),
    path('create/', views.create, name='create_todo'),
    # path('<int:todo_id>/', views.change_status, name='change_status'),
]