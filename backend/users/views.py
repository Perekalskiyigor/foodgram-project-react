# from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def FollowListView(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def FollowViewSet(request):
    return HttpResponse('Список мороженого')


# Create your views here.
