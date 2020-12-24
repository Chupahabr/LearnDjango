from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='learn'),
    path('<int:pk>', views.newDetailView.as_view(), name='news_detail'),
    path('search', views.search, name='search'),
]