-- Εισάγουμε μία νέα πτήση στη βάση δεδομένων
INSERT INTO flights
    (origin, destination, duration)
    VALUES ("new york", "london", 415);

-- Εμφανίζουμε όλες τις πτήσεις
SELECT * FROM flights;

-- Εμφανίζουμε μόνο την προέλευση και τον προορισμό από τον πίνακα πτήσεων
SELECT origin, destination FROM flights;

-- Επιλέγουμε τη πτήση με το id 3
SELECT * FROM flights WHERE id = 3;

-- Επιλέγουμε πτήσεις με διάρκεια μεγαλύτερη από 500 και προορισμό το Παρίσι
SELECT * FROM flights WHERE duration > 500 AND destination = "paris";

-- Επιλέγουμε πτήσεις όπου η προέλευση περιέχει το γράμμα "a"
SELECT * FROM flights WHERE origin LIKE "%a%";

-- Το % αντιπροσωπεύει 0 ή περισσότερους χαρακτήρες

-- Ενημερώνουμε τη διάρκεια της πτήσης από τη Νέα Υόρκη στο Λονδίνο
UPDATE flights
    SET duration = 430
    WHERE origin = "new york"
    AND destination = "london";

-- Διαγράφουμε τις πτήσεις με προορισμό το Τόκιο
DELETE FROM flights WHERE destination = "tokio";

-- Δημιουργούμε ένα νέο αρχείο βάσης δεδομένων
$ touch flights.sql

-- Εκκινούμε το SQLite3 με το αρχείο flights.sql
$ sqlite3 flights.sql

-- Δημιουργούμε πίνακα πτήσεων με id, origin, και destination
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Το πεδίο id θα αυξάνεται αυτόματα
    origin TEXT NOT NULL, -- Το πεδίο origin είναι απαραίτητο
    destination TEXT NOT NULL, -- Το πεδίο destination είναι επίσης απαραίτητο
    duration INTEGER -- Το πεδίο duration αποθηκεύει τη διάρκεια της πτήσης
);

-- Προβολή όλων των πινάκων της βάσης δεδομένων
.tables

-- Αλλαγή του τρόπου εμφάνισης σε στήλες
.mode columns

-- Εμφάνιση των επικεφαλίδων των στηλών
.headers yes

-- Σχέσεις μεταξύ πινάκων
SELECT first, origin, destination
    FROM flights JOIN passengers
    ON passengers.flight_id = flights.id;
-- Συνδέουμε τους πίνακες flights και passengers μέσω του flight_id

-- Δημιουργούμε index για το πεδίο last των επιβατών
CREATE INDEX name_index ON passengers (last);

-- Επίθεση SQL injection - Παράδειγμα κακής πρακτικής
SELECT * FROM users
WHERE username = "alkis" AND password = "1234";
-- Ευάλωτος κώδικας σε επιθέσεις SQL injection

# Django models

-- Δημιουργούμε ένα νέο project Django
django-admin startproject airline

-- Δημιουργούμε μία νέα εφαρμογή πτήσεων
python manage.py startapp flights

-- Προσθέτουμε την εφαρμογή στη λίστα installed_apps του project

-- Δημιουργούμε νέα διαδρομή για την εφαρμογή flights
path("flights/", include("flights.urls"))

# urls.py
urlpatterns += [

]

# models.py

-- Δημιουργούμε το μοντέλο πτήσης
class Flight(models.Model):
    origin = models.CharField(max_length=64)  # Το πεδίο origin είναι κείμενο μέχρι 64 χαρακτήρες
    destination = models.CharField(max_length=64)  # Το πεδίο destination είναι κείμενο μέχρι 64 χαρακτήρες
    duration = models.IntegerField()  # Το πεδίο duration αποθηκεύει ακέραιους αριθμούς

-- Εφαρμόζουμε τις αλλαγές στο μοντέλο
python manage.py makemigrations
python manage.py migrate

-- Δημιουργούμε νέα πτήση μέσω του Django shell
from flights.models import Flight
f = Flight(origin="new york", destination="london", duration=415)
f.save()

-- Εμφανίζουμε όλες τις πτήσεις
Flight.objects.all()  # Αντιστοιχεί στο SELECT * FROM flights

-- Προσθέτουμε μέθοδο __str__ για καλύτερη αναπαράσταση
def __str__(self):
    return f"{self.id}: {self.origin} to {self.destination}"

# Δημιουργία του μοντέλου αεροδρομίου
class Airport(models.Model):
    code = models.CharField(max_length=3)  # Το πεδίο code περιέχει 3 χαρακτήρες για τον κωδικό του αεροδρομίου
    city = models.CharField(max_length=64)  # Το πεδίο city αποθηκεύει την πόλη

    def __str__(self):
        return f"{self.city} ({self.code})"

# Ενημερώνουμε το μοντέλο Flight ώστε να περιλαμβάνει Foreign Keys προς το μοντέλο Airport
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

-- Εφαρμόζουμε τις αλλαγές στο μοντέλο
python manage.py makemigrations
python manage.py migrate

-- Δημιουργούμε νέα εγγραφή αεροδρομίου και την χρησιμοποιούμε για την δημιουργία νέας πτήσης
jfk = Airport(code="JFK", city="New York")
f = Flight(origin=jfk, destination=jfk, duration=415)
f.save()

# urls.py

-- Δημιουργούμε διαδρομές (URL patterns) για το αρχείο urls.py
urlpatterns = [
    path("", view.index, name="index")
]

# views.py

-- Δημιουργούμε την όψη (view) για την αρχική σελίδα
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

# HTML Template (flights/index.html)

-- Προβάλλουμε όλες τις πτήσεις μέσα από το Django template
{% for flight in flights %}
    <li> Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}</li>
{% endfor %}

-- Εκκινούμε τον διακομιστή Django
python manage.py runserver

# django admin app
python manage.py createsuperuser

-->admin.py
import .models import FLights, Airport

#register model
admin.site.register(Airport)
admin.site.register(Flights)
# --> pao url /admin
# Αυτό το τμήμα κώδικα ορίζει τις διαδρομές (URLs) της εφαρμογής.

urlpaterns = [
    path("<int:flight_id>", views.flight, name="flight")  # Η διαδρομή δέχεται έναν ακέραιο αριθμό για το flight_id και καλεί τη συνάρτηση flight στο views.
]

# --> views
def flight(request, flight_id):
    # Ανάκτηση της πτήσης από τη βάση δεδομένων βάσει του flight_id.
    flight = Flight.objects.get(id=flight_id)

    # Επιστροφή της απόκρισης που περιλαμβάνει τα δεδομένα της πτήσης και τους επιβάτες.
    return render(request, "flights/flight.html", {
        "flight": flight,  # Παράδοση του αντικειμένου flight στο πρότυπο HTML.
        "passengers": flight.passengers.all(),  # Όλοι οι επιβάτες της πτήσης.
        "non_passengers": Passenger.objects.exclude(flights=flight)  # Επιβάτες που δεν ανήκουν στην τρέχουσα πτήση.
    })

# --> html
# Κώδικας HTML για την προβολή πληροφοριών της πτήσης και των επιβατών.

<h1> Flight {{ flight.id }} </h1>  # Εμφάνιση του ID της πτήσης.
<ul>
    <li>origin: {{ flight.origin }}</li>  # Πηγή της πτήσης.
    <li>destination: {{ flight.destination }}</li>  # Προορισμός της πτήσης.
    <li>duration: {{ flight.duration }}</li>  # Διάρκεια της πτήσης.
</ul>

<h2>passengers</h2>
<ul>
    {% for passenger in passengers %}  # Επανάληψη για όλους τους επιβάτες.
        <li>{{ passenger }}</li>
    {% endfor %}
</ul>

<h2>add passenger</h2>
# Φόρμα για την προσθήκη επιβάτη.
<form action="{% url 'book' flight.id %}" method="post">
    {% csrf_token %}  # Προστασία από επιθέσεις CSRF.
    <select name="passenger">
        {% for passenger in non_passengers %}  # Επιλογή επιβάτη που δεν έχει ήδη προστεθεί.
            <option value={{ passenger.id }}>{{ passenger }}</option>
        {% endfor %}
    </select>
    <input type="submit">
</form>

<a href="{% url 'index' %}">back to flight list</a>  # Σύνδεσμος για την επιστροφή στη λίστα πτήσεων.

# --> models.py many-to-many relations
# Δημιουργία μοντέλου για τους επιβάτες με ManyToManyField για συσχετισμό με πτήσεις.

class Passenger(models.Model):
    first = models.CharField(max_length=64)  # Όνομα επιβάτη.
    last = models.CharField(max_length=64)  # Επώνυμο επιβάτη.
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")  # Πτήσεις στις οποίες συμμετέχει ο επιβάτης.

    def __str__(self):
        return f"{self.first} ({self.last})"  # Επιστροφή της συμβολοσειράς για την αναπαράσταση του επιβάτη.

# Εντολές για τη διαχείριση των μεταναστεύσεων στη βάση δεδομένων.
python manage.py makemigrations
python manage.py migrate

# --> urls.py
# Ορισμός της διαδρομής για την κράτηση επιβάτη σε πτήση.

path("int:flight_id/book", views.book, name="book")

# --> views
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)  # Το pk είναι το ίδιο με το id της πτήσης.
        passenger = Passenger.objects.get(id=request.POST["passenger"])  # Ανάκτηση του επιβάτη βάσει του id.
        passenger.flights.add(flight)  # Προσθήκη της πτήσης στον επιβάτη (many-to-many).

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))  # Ανακατεύθυνση πίσω στη σελίδα της πτήσης.

# ---> users<---
# Δημιουργία νέας εφαρμογής "users" για διαχείριση χρηστών.
python manage.py startapp users

# --> settings.py
# Προσθήκη της εφαρμογής "users" στο αρχείο ρυθμίσεων.
# --> urls.py
path("users/", include("users.urls"))

# --> users/urls.py
# Διαδρομές για την εφαρμογή "users".
urlpatterns = [
    path("", views.index, name="index"),  # Αρχική σελίδα χρηστών.
    path("login", views.login_view, name="login"),  # Σελίδα σύνδεσης.
    path("logout", views.logout_view, name="logout")  # Σελίδα αποσύνδεσης.
]

# --> views
def index(request):
    if not request.user.is_authenticated:  # Έλεγχος αν ο χρήστης έχει συνδεθεί.
        return HttpResponseRedirect(reverse("login"))  # Ανακατεύθυνση στη σελίδα σύνδεσης αν δεν είναι συνδεδεμένος.
    return render(request, "users/user.html")  # Εμφάνιση της σελίδας χρήστη αν είναι συνδεδεμένος.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]  # Ανάκτηση του ονόματος χρήστη από τη φόρμα.
        password = request.POST["password"]  # Ανάκτηση του κωδικού πρόσβασης από τη φόρμα.
        user = authenticate(request, username=username, password=password)  # Έλεγχος αν τα διαπιστευτήρια είναι σωστά.
        if user is not None:
            login(request, user)  # Σύνδεση του χρήστη.
            return HttpResponseRedirect(reverse("index"))  # Ανακατεύθυνση στην αρχική σελίδα.
        else:
            return render(request, "users/login.html", {
                "message": "Invalid"  # Μήνυμα λάθους αν τα διαπιστευτήρια είναι λάθος.
            })
    return render(request, "users/login.html")  # Εμφάνιση της φόρμας σύνδεσης.

def logout_view(request):
    logout(request)  # Αποσύνδεση του χρήστη.
    return render(request, "users/login.html", {
        "message": "logged out"  # Μήνυμα επιβεβαίωσης αποσύνδεσης.
    })

# --> login.html
# Πρότυπο HTML για τη σελίδα σύνδεσης.

{% if message %}
    <div>{{ message }}</div>  # Εμφάνιση του μηνύματος λάθους ή αποσύνδεσης.
{% endif %}

<form action="{% url 'login' %}" method="post">
    {% csrf_token %}  # Προστασία από επιθέσεις CSRF.
    <input type="text" name="username" placeholder="username">  # Πεδίο για το όνομα χρήστη.
    <input type="password" name="password" placeholder="password">  # Πεδίο για τον κωδικό πρόσβασης.
    <input type="submit" value="login">  # Κουμπί για την υποβολή της φόρμας.
</form>

#---> admin



as a review of this lesson create me the simplest simplest simplest example that uses django, has two (easy) models, retrieves and saves data to them and has two htm pages where info from one is sended to other
Το ChatGPT είπε:
ChatGPT
Let's create a simple Django project with two models, where one page sends data to the other and the data gets saved and displayed.

Project Overview:
Two models: Book and Author.
Two pages:
A form to create a new book with a title and select an author.
A page to display the saved books and their authors.
Steps:
1. Setup Django Project
bash
Αντιγραφή κώδικα
django-admin startproject mysite
cd mysite
python manage.py startapp library
2. Define Models
In library/models.py, define the Author and Book models:

python
Αντιγραφή κώδικα
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
3. Register Models in Admin
In library/admin.py, register the models so you can add authors from the admin page:

python
Αντιγραφή κώδικα
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
4. Create Views
In library/views.py, create two views:

Add Book: A form to create a new book.
Display Books: A page to display the list of books.
python
Αντιγραφή κώδικα
from django.shortcuts import render, redirect
from .models import Author, Book

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('books')  # After saving, redirect to the list of books

    authors = Author.objects.all()
    return render(request, 'library/add_book.html', {'authors': authors})

def display_books(request):
    books = Book.objects.all()
    return render(request, 'library/books.html', {'books': books})
5. Create URLs
In library/urls.py, define the URLs for the views:

python
Αντιγραφή κώδικα
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('books/', views.display_books, name='books'),
]
In mysite/urls.py, include the library app's URLs:

python
Αντιγραφή κώδικα
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
]
6. Create HTML Templates
Add Book Form (library/templates/library/add_book.html):
html
Αντιγραφή κώδικα
<h1>Add a Book</h1>
<form method="POST">
    {% csrf_token %}
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required><br><br>

    <label for="author">Author:</label>
    <select id="author" name="author" required>
        {% for author in authors %}
            <option value="{{ author.id }}">{{ author.name }}</option>
        {% endfor %}
    </select><br><br>

    <input type="submit" value="Add Book">
</form>
<a href="{% url 'books' %}">View All Books</a>
Display Books (library/templates/library/books.html):
html
Αντιγραφή κώδικα
<h1>List of Books</h1>
<ul>
    {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
    {% endfor %}
</ul>
<a href="{% url 'add_book' %}">Add a New Book</a>
7. Migrate and Run the Project
bash
Αντιγραφή κώδικα
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
8. Admin Setup
Go to /admin, add some authors, and then test the application by going to /add/ to create a book and /books/ to see the list of books.
