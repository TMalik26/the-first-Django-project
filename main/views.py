from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'HappyToes'
        context['content'] = 'Магазин носочків для легкої ходи - HappyToes'
        context['categories'] = Categories.objects.all()
        return context


# def index(request):
#     
#     context = {
#         'title' : 'HappyToes',
#         'content' : 'Магазин носочків для легкої ходи - HappyToes',
#     }
#     return render(request, 'main/index.html', context=context)


class AboutView(TemplateView):
    template_name = 'main/about.html'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'HappyToes'
        return context


# def about(request):
#     context = {
#         'title' : 'HappyToes',
#     }
#     return render(request, 'main/about.html', context=context)