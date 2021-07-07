from django.shortcuts import render
from .models import *



def main(request):
    news = News.objects.order_by('-create_at')
    context = {
        "news" : news,
    }
    return render(request, template_name='blog/index.html', context=context)