from django.shortcuts import render, redirect

from .models import *

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    content = {
        "maqolalar": Maqola.objects.all()
    }
    return render(request, "blog.html", content)

def maqola(request):
    content = {
        "maqola": Maqola.objects.all()
    }
    return render(request, "maqola.html", content)

def t_maqola(request, son):
    Maqola.objects.get(id=son)
    return redirect("/maqola/")