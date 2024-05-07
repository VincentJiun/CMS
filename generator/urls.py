from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passwd/', views.passwd, name='passwd'),
]