# python manage.py runserver
# python manage.py startapp hello

1. Django Template Syntax

{% extends "path/to/template.html" %}:
Purpose: This tag is used to specify that the current template extends another template. It helps in reusing common layout code across multiple templates.
Example: {% extends "tasks/layout.html" %}

{% block blockname %}:
Purpose: Defines a block in a template that can be overridden in child templates. It is used in conjunction with {% extends %}.
Example: {% block body %}

{% endblock %}:
Purpose: Ends a block definition started by {% block blockname %}.
Example: {% endblock %}

{% for item in items %}:
Purpose: Starts a loop that iterates over a list or queryset.
Example: {% for task in tasks %}

{% empty %}:
Purpose: Provides content to be displayed if the loop iterates over an empty list.
Example: {% empty %} <li>No tasks</li>

{% url 'namespace:name' %}:
Purpose: Generates a URL for a view based on its name and optional namespace. It is used to create links to views.
Example: {% url 'tasks:add' %}

{{ form }}:
Purpose: Renders a Django form in the template, displaying all form fields and associated error messages.
Example: {{ form }}

{% csrf_token %}:
Purpose: Inserts a CSRF token into forms to protect against Cross-Site Request Forgery attacks.
Example: {% csrf_token %}

2. Python Syntax in Django Views

request.method == "POST":
Purpose: Checks if the request method is POST, indicating that the form has been submitted.
Example: if request.method == "POST":

form.is_valid():
Purpose: Checks if the submitted form data is valid according to the form’s validation rules.
Example: if form.is_valid():

form.cleaned_data:
Purpose: Provides access to the validated form data. The keys are field names defined in the form.
Example: task = form.cleaned_data["task"]

request.session:
Purpose: Accesses the session dictionary, which allows you to store and retrieve data specific to a user session.
Example: request.session["tasks"] += [task]

HttpResponseRedirect(reverse('viewname')):
Purpose: Redirects to a different URL after processing a form. reverse is used to dynamically generate the URL based on view names.
Example: return HttpResponseRedirect(reverse("tasks:index"))
3. HTML Syntax
<!-- Comment -->:
Purpose: Inserts comments into HTML code that are not displayed in the browser but can be seen in the source code.
Example: <!-- This is a comment -->

"""
Here's a step-by-step summary of how the "hello" app was initialized in Django:

Create the Django Project:
Run django-admin startproject lecture3 to create a new Django project named lecture3.

Create the Django App:
Navigate to the project directory and run python manage.py startapp hello to create a new app named hello within the project.

Add the App to the Project:
Open lecture3/settings.py and add 'hello' to the INSTALLED_APPS list to include the new app in the project.

Define a View in the App:
Open hello/views.py and create a view function named index that returns HttpResponse("Hello, world!").

Configure URLs for the App:
Create a file hello/urls.py and define a URL pattern to map the root URL (empty string) to the index view. Use path('', views.index, name='index') and import the views from hello.

Include the App's URLs in the Project:
Open lecture3/urls.py and include the app's URL patterns by adding path('hello/', include('hello.urls')) to the urlpatterns list.

"""

"""

URL Routing:

urls.py in lecture3: This is the main URL configuration file where you map URL patterns to applications. You’ve mapped the /hello route to your hello application, which has its own URLs configuration.
urls.py in hello: Inside the hello app, you defined multiple routes. For instance:
/hello/ -> Loads the index function in views.py that returns a simple response.
/hello/brian -> Loads the brian function.
Dynamic URLs like /hello/<name> can greet any name by calling a function (greet) that uses Django's templating system to create dynamic responses.

Views and Responses:

Views in views.py: The views.py file contains functions like index, brian, and greet. Each function processes an incoming HTTP request and returns an HTTP response. The greet function dynamically greets any name by using a URL parameter.
HttpResponse: Initially, your views returned plain text responses (e.g., "Hello, world!"). Later, you shifted to using Django’s render function to render HTML templates.

Templates:

Dynamic HTML with Django's Template Language: You created templates that dynamically insert variables into HTML pages. For example, the greet function passes the name to greet.html, which uses {{ name }} to display the name within an HTML structure.
Separation of Concerns: By moving HTML to templates, you separate the presentation layer (HTML) from the business logic (views). This keeps your code cleaner and easier to maintain.

Context and Templating Language:

Context Dictionary: In the greet view, you pass a dictionary ({'name': name.capitalize()}) to the render function. This dictionary contains variables that the template can access (e.g., the name to greet).
Template Rendering: Django uses its templating language to inject the variable into the HTML. For instance, the {{ name }} in greet.html gets replaced with the actual name provided in the URL.

Advanced Django Templating:

You touched on how Django's templating system can do more than just display variables. It can also handle logic like loops, conditions, etc., making it a powerful tool for generating dynamic web content.

"""

# python manage.py startapp newyear

"""

o create a simple "Is it New Year?" Django web application, follow these steps, adapting it to a similar structure as outlined in the example above:

1. Create a new Django app
Run this command to create a new app named newyear:

bash
Αντιγραφή κώδικα
python manage.py startapp newyear
2. Add the app to INSTALLED_APPS in settings.py
Edit your settings.py file and add 'newyear' to INSTALLED_APPS:

python
Αντιγραφή κώδικα
INSTALLED_APPS = [
    ...
    'newyear',
]
3. Set up URLs
In your project’s main urls.py file, add a route for your newyear app:

python
Αντιγραφή κώδικα
from django.urls import include, path

urlpatterns = [
    ...
    path('newyear/', include('newyear.urls')),
]
Now, in your newyear app, create a new file urls.py:

python
Αντιγραφή κώδικα
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
4. Create the view
In views.py of the newyear app, create the index view:

python
Αντιγραφή κώδικα
from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    newyear = (now.month == 1 and now.day == 1)
    return render(request, 'newyear/index.html', {
        'newyear': newyear
    })
5. Create the HTML template
Inside your newyear app, create a directory named templates/newyear/, and inside it, create a file index.html:

html
Αντιγραφή κώδικα
<!DOCTYPE html>
<html>
    <head>
        <title>Is it New Year's?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
6. (Optional) Add some styling
You can add a CSS file by creating a static/newyear/ folder in your newyear app and adding a styles.css file. Here’s a sample:

css
Αντιγραφή κώδικα
h1 {
    font-family: sans-serif;
    font-size: 90px;
    text-align: center;
}
In index.html, make sure to load the CSS by adding this in the <head> section:

html
Αντιγραφή κώδικα
{% load static %}
<link rel="stylesheet" href="{% static 'newyear/styles.css' %}">
7. Run the server
Start the Django development server:

bash
Αντιγραφή κώδικα
python manage.py runserver
Visit http://127.0.0.1:8000/newyear/ to see if it's New Year's or not!

"""

# python manage.py startapp tasks

# template inheritance
