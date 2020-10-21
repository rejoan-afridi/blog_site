from django.shortcuts import render, HttpResponse
from main.models import *
from main.models import Category

# Create your views here.


def index(request):
    all_post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "blog": all_post,
        "category": categories
    }
    return render(request, 'main/index.html', context)


def details(request):
    return render(request, 'main/blogview.html')


def post(request, slug_text):
    querry = Post.objects.filter(slug=slug_text)
    categories = Category.objects.all()
    # querry.views = querry.views + 1
    context = {
        'post': querry,
        'category': categories


    }
    return render(request, 'main/blogview.html', context)
