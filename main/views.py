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

    # if 'category' in request.GET:
    #     category_id = request.GET['category']
    #     category = Category.objects.get(id=category_id)
    #     post = Post.objects.filter(category_id=category_id)
    #     context = {
    #         "category": category,
    #         "blog": post
    #     }
    #     return render(request, 'main/blogview.html', context)
    # else:
        return render(request, 'main/blogview.html')


def post(request, slug_text):
    querry = Post.objects.filter(slug=slug_text)
    categories = Category.objects.all()
    context = {
        'post': querry,
        'category':categories
      
        
    }
    return render(request, 'main/blogview.html', context)
