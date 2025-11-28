from django.shortcuts import render

from goods.models import Categories

def index(request):
    categories = Categories.objects.all()

    context = {
        'title' : 'HappyToes',
        'content' : 'Магазин носків - HappyToes',
        'categories': categories
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'title' : 'HappyToes',
    }
    return render(request, 'main/about.html', context=context)
[]