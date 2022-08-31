# from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def apiview(request):    
    return HttpResponse('API')
