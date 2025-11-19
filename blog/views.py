from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def inicio(request):
    mensaje = "Bienvenido a mi blog usando Django"
    numero = 10 
    post = Post.objects.all()

    contexto = {
        "mensaje" : mensaje,
        "numero" : numero,
        "posts" : post,
    }
    return render(request, "blog/index.html",contexto)

def about(request):
    return render(request, "blog/about.html")
