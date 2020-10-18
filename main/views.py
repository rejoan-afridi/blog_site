from django.shortcuts import render, HttpResponse
from main.models import *
from main.models import Category

# Create your views here.


def index(request):
    all_category = Post.objects.all()
    context = {
        "blog": all_category
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
    context = {
        'post': querry,
      
        
    }
    return render(request, 'main/blogview.html', context)
