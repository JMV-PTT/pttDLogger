from django.urls import path, include, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    # re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.article_detail, name='detail'),
    # path('<slug>/', views.article_detail, name='detail'),
]
