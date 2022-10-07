from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('oder/', views.oder, name='oder'),
    path('about/', views.aboutus, name='us'),
    path('books/', views.book_list, name='book_list'),
]
