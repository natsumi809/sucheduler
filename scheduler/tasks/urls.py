from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task_date/', views.update_task_date, name='update_task_date'),
    path('remove_task_date/', views.remove_task_date, name='remove_task_date'),
    path('delete_task/', views.delete_task, name='delete_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/', views.edit_task, name='edit_task'),
    path('delete_all_todo/', views.delete_all_todo, name='delete_all_todo'),
    path('update_task_duration/', views.update_task_duration, name='update_task_duration'),
]