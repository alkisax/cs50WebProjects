from django.urls import path  # Imports the path function used to define URL patterns
from . import views  # Imports the views module from the current package

app_name = "tasks"  # Namespaces the URL patterns for this app, allowing for more organized URL management

urlpatterns = [  # List of URL patterns for this app
    path("", views.index, name="index"),  # Maps the root URL of the 'tasks' app to the 'index' view function and names this URL pattern 'index'
    path("add", views.add, name="add"),  # Maps the 'add' URL to the 'add' view function and names this URL pattern 'add'
]


