from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.view_todo, name='view_todo'),
    path('create/', views.create_todo, name='create_todo'),
    path('complete/', views.complete_todo, name='complete'),
    path('delete/<int:id>', views.delete, name='delete'),
]