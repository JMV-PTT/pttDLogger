from django.urls import path, include
from . import views

app_name = 'tlog'

urlpatterns = [
    path('', views.log_list, name='dataLog'),
    path('dQ/', views.regD, name='dataUp'),
    path('<slug:slug>/', views.log_d, name='dataDetail'),

]
