from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alkis", views.alkis, name="alkis"),
    path("<str:name>", views.greet, name="greet"),
]
