from django.urls import path
from . import views
urlpatterns = [
    path('main/main', views.index, name='index'),
    path('main/about', views.about, name='about'),
]
