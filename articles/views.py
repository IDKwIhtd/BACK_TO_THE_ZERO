from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse("<h1>Hey, There!</h1>")
    return response

def index2(request):
    return render(request, 'index2.html')

def users(request):
    return render(request, 'users.html')

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