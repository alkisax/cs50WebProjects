from django.shortcuts import render  # Importing the `render` function to render HTML templates
from django import forms  # Importing Django's forms module to create forms
from django.http import HttpResponseRedirect  # Importing to handle HTTP redirects after form submission
from django.urls import reverse  # Importing `reverse` to generate URLs based on the URL patterns and view names για να χρησιμοποιώ το ονομα του url και οχι το ιδιο url

# Create your views here.

# tasks = ["foo", "bar", "baz", "bak"]  # This was a simple list for storing tasks before using sessions, now commented out

# Define a form class for adding new tasks
class NewTaskForm(forms.Form):  # Inherits from `forms.Form`, which is the base class for creating forms in Django
    task = forms.CharField(label="New Task")  # Creates a single form field, a CharField (text input), labeled "New Task"
    # priority = forms.IntegerField(label="priority", min_value=1, max_value=10)  # An optional field for priority, commented out αν θέλω με αυτό τον τροπο μπορώ να προσθέσω περισσότερα fields εδώ και όχι κατ αναγκη στην html σελιδα μου

# The index view renders the list of tasks and checks if "tasks" exist in the session
def index(request):
    # If the "tasks" key doesn't exist in the session, initialize it as an empty list
    if "tasks" not in request.session:
        request.session["tasks"] = []  # This stores the tasks in the session to persist across requests

    # Render the "index.html" template with the current tasks (stored in the session) passed to the context
    return render(request, "tasks/index.html", {
        # "tasks": tasks  # Originally used to pass the commented out `tasks` list, but now using session storage
        "tasks": request.session["tasks"]  # The tasks stored in the session are passed to the template
    })

# The add view handles form submissions for adding new tasks
def add(request):
    # If the request method is POST, the form was submitted
    if request.method == "POST":
        form = NewTaskForm(request.POST)  # Populate the form with POST data to validate the form submission
        if form.is_valid():  # Check if the form is valid (i.e., conforms to the rules of the form fields)
            task = form.cleaned_data["task"]  # Extract the validated data from the form (task text)

            # The following line appends the new task to the session's "tasks" list
            # `request.session["tasks"] += [task]` adds the new task as a list (ensures it's a list addition, not string concatenation)
            request.session["tasks"] += [task]

            # Redirect the user back to the "tasks:index" view after successfully adding the task
            # `reverse("tasks:index")` generates the URL for the "index" view based on its name in the URLconf
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # If the form is not valid, render the form again on the "add" page, with error messages
            return render(request, "tasks/add.html", {
                "form": form  # Pass the form (which contains the errors) back to the template
            })

    # If the request method is GET (i.e., the user is just visiting the page), show an empty form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()  # Pass a new, empty form to the template
    })
