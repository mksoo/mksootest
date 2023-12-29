from django.urls import path

from . import views

# app 단위에서 routing
urlpatterns = [
    path('', views.index, name='index'),
    path('home/v1', views.h2, name='h2')
]
