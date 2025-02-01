from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    response = HttpResponse("<h1>Hey, There!</h1>")
    return response

def index2(request):
    return render(request, 'articles/index2.html')

def hello(request):
    name = "BIBI"
    tags = ['python', 'django', 'git']
    techs = {'frontend': 'HTML, CSS, JS', 'backend': 'Python, Django, FASTAPI'}
    context = {"name" : name,
               "tags" : tags,
               "techs" : techs}
    return render(request, 'articles/hello.html', context)

def data_throw(request):
    return render(request, 'articles/data_throw.html')

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "data" : message,
    }
    return render(request, 'articles/data_catch.html', context)

def articles(request):
    articles = Article.objects.all().order_by("-id")
    context = {
        "articles":articles,
    }
    return render(request, 'articles/articles.html', context)

def create(request):
    if request.method =="POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm()

    context = {"form":form}
    return render(request, "articles/create.html", context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         "form":form,
#     }
#     return render(request, 'new.html', context)

# def create(request):
#     form = ArticleForm(request.POST) #form에 request.POST에 있는 데이터 채워서
#     if form.is_valid(): # form 형식에 맞으면
#         article = form.save() #저장 후 해당 객체 반환
#         return redirect("article_detail", article.id)
#     return redirect("new")

# def create(request):
#     title = request.POST.get("title")
#     content = request.POST.get("content")

#     article = Article(title=title, content =content)
#     article.save()
#     context = {
#         "article":article,
#     }
#     return render(request, "create.html", context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article,
    }
    return render(request, "article_detail.html", context)

# def create(request):
#     title = request.POST.get("title")
#     content =request.POST.get("content")
#     article = Article(title=title, content = content)
#     article.save()
#     return redirect("article_detail", article.id)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:articles")
    return redirect("articles:article_detail", article.pk)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context ={
#         "article":article,
#     }
#     return render(request, "edit.html", context)

# def update(request, pk):
#     article=Article.objects.get(pk=pk)
#     article.title=request.POST.get("title")
#     article.content=request.POST.get("content")
#     article.save()
#     return redirect("article_detail", article.pk)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
        context = {
            "form":form,
            "article":article,
        }
        return render(request, "articles/update.html", context)
