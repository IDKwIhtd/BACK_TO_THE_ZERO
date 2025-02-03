from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

        
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index2")

# def logout(request):
#     if request.method=="POST":
#         auth_logout(request)
#     return redirect("articles:index2")








# def login(request):
#     form = AuthenticationForm()
#     context = {"form":form}
#     return render(request, "accounts/login.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path = request.GET.get("next") or "index2"
            return redirect("articles:index2")
    else:
        form = AuthenticationForm()
    context = {"form":form}
    return render(request, "accounts/login.html", context)



