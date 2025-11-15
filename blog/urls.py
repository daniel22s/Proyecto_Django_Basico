from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('about/',views.about,name='about'),
    path('lista_posts/',views.lista_posts,name='lista_posts'),
]
