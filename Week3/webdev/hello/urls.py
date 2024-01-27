from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("eizad", views.eizad, name="eizad"),
    path("eizad/hamdan", views.hamdan, name="hamdan"),
    path("<str:name>", views.greet, name="greet"),
]