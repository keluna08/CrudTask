from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:id>/', views.task_detail, name='task_detail'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:id>/', views.task_edit, name='task_update'),
    path('delete/<int:id>/', views.delete, name='task_delete'),

]
