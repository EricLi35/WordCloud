from django.contrib import admin
from django.urls import path, include
from appName import views

urlpatterns = [
    path('' , views.wordcloud2 , name='')
]
