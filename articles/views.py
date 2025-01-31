from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    response = HttpResponse("<h1>Hey, There!</h1>")
    return response

def index2(request):
    return render(request, 'index2.html')

def hello(request):
    name = "BIBI"
    tags = ['python', 'django', 'git']
    techs = {'frontend': 'HTML, CSS, JS', 'backend': 'Python, Django, FASTAPI'}
    context = {"name" : name,
               "tags" : tags,
               "techs" : techs}
    return render(request, 'hello.html', context)

def data_throw(request):
    return render(request, 'data_throw.html')

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "data" : message,
    }
    return render(request, 'data_catch.html', context)

def articles(request):
    articles = Article.objects.all().order_by("-id")
    context = {
        "articles":articles,
    }
    return render(request, 'articles.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article(title=title, content =content)
    article.save()
    context = {
        "article":article,
    }
    return render(request, "create.html", context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article,
    }
    return render(request, "article_detail.html", context)

def create(request):
    title = request.POST.get("title")
    content =request.POST.get("content")
    article = Article(title=title, content = content)
    article.save()
    return redirect("article_detail", article.id)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles")
    return redirect("article_detail", article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context ={
        "article":article,
    }
    return render(request, "edit.html", context)

def update(request, pk):
    article=Article.objects.get(pk=pk)
    article.title=request.POST.get("title")
    article.content=request.POST.get("content")
    article.save()
    return redirect("article_detail", article.pk)
