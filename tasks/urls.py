from django.contrib import admin
from django.urls import path
from tasks.views import task_list, add_task


urlpatterns = [
    path('', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
]