from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.http import HttpResponseForbidden


# Create your views here.
@require_POST
def like(request, pk):
    if not request.user.is_authenticated:
        return redirect("accounts:login")  # 로그아웃 상태에서는 로그인 페이지로 이동

    article = get_object_or_404(Article, pk=pk)

    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    return redirect("articles:articles")  # 리스트 페이지로 리디렉트 (좋아요 반영)


def delete_image(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        # 기존 이미지 삭제
        if article.image:
            article.image.delete()  # 이미지 파일 삭제
            article.image = None  # DB에서도 삭제
            article.save()

    return redirect("articles:update", article.pk)  # 이미지 삭제 후, 수정 페이지로 이동


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)  # DB에 저장하지 않고 객체만 생성
            article.author = request.user  # 작성자를 현재 로그인한 유저로 설정
            article = form.save()  # DB에 저장
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 최신 댓글이 위로 오도록 정렬
    comments = article.comment_set.all().order_by("-created_at")

    comment_form = CommentForm()
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/article_detail.html", context)


# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         "article": article,
#     }
#     return render(request, "articles/article_detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if article.author != request.user:  # 작성자가 아니면 수정 불가
        return HttpResponseForbidden("수정할 권한이 없습니다.")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
        context = {
            "form": form,
            "article": article,
        }
        return render(request, "articles/update.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user:
            article.delete()
        else:
            return HttpResponseForbidden("이 게시글을 삭제할 권한이 없습니다.")
    return redirect("articles:articles")


def index(request):
    response = HttpResponse("<h1>Hey, There!</h1>")
    return response


def index2(request):
    return render(request, "articles/index2.html")


def hello(request):
    name = "BIBI"
    tags = ["python", "django", "git"]
    techs = {"frontend": "HTML, CSS, JS", "backend": "Python, Django, FASTAPI"}
    context = {"name": name, "tags": tags, "techs": techs}
    return render(request, "articles/hello.html", context)


def data_throw(request):
    return render(request, "articles/data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "data": message,
    }
    return render(request, "articles/data_catch.html", context)


def articles(request):
    articles = Article.objects.all().order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


# def create(request):
#     if request.method =="POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             return redirect("articles:article_detail", article.id)
#     else:
#         form = ArticleForm()

#     context = {"form":form}
#     return render(request, "articles/create.html", context)

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

# def create(request):
#     title = request.POST.get("title")
#     content =request.POST.get("content")
#     article = Article(title=title, content = content)
#     article.save()
#     return redirect("article_detail", article.id)

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


# def article_detail(request, pk):
#     article = get_object_or_404(Article,pk=pk)
#     context = {
#         "article" : article,
#     }
#     return render(request, "articles/article_detail.html", context)


@require_POST
@login_required
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # DB에 저장 전에 객체 생성
        comment.author = request.user  # 현재 로그인한 사용자 설정
        comment.article = article  # article 필드 직접 할당
        comment.save()  # 최종 저장
    return redirect("articles:article_detail", pk=article.pk)


@require_POST
@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    article_pk = comment.article.pk
    if request.user == comment.author:
        comment.delete()
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")
    return redirect("articles:article_detail", pk=article_pk)
