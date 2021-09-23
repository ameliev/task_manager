from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:id>', views.show_task, name="showTask"),
    path('tasks/<int:user_id>', views.tasks_list, name="tasksList"),
    path('task/<int:user_id>/new', views.new_task, name="newTask"),
    path('task/<int:pk>/edit/', views.edit_task, name='editTask'),
    path('task/<int:pk>/remove/', views.remove_task, name='removeTask'),
    path('task/<int:pk>/done/', views.done_task, name='doneTask'),
]
