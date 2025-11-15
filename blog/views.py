from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def inicio(request):
    return HttpResponse(
                        '<h1>Hola, Bienvenido a mi primer Blog</h1>'
                        '<a href="templates/blog/lista_posts.html">Lista de Posts</a>'
)

def about(request):
    return HttpResponse("<h2>About</h2>")

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request,"blog/lista_posts.html"   ,{"posts":posts})