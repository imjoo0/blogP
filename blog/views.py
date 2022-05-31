from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Category
from .models import Article

def home(request):
    return render(request,'base.html')


def new_blog(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        desc = request.POST.get('desc', None)
        category = request.POST.get('category', None)

        new_Article = Article()
        new_Article.title=title
        new_Article.entertain = desc
        new_Article.category = category
        new_Article.save()

        return redirect('/home')
