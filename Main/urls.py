from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('read/<int:id>', views.read, name="read"),
    path('signup', views.signup, name='signup'), # дабы не создавать новый view в корне, из-за отстутсвия реализации регистрации
                                                  # вне админ панели, форма регистрации помещена в "главное приложение"
    path('my_courses', views.my_courses, name='my_courses'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit")

]

