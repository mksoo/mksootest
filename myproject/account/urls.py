from django.urls import path

from . import views

urlpatterns = [
    path("home/page/", views.hello_world, name="account home page")
]
