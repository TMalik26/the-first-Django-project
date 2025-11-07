from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title' : 'HappyToes',
        'content' : 'Головна'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title' : 'HappyToes',
    }
    return render(request, 'main/about.html', context=context)
