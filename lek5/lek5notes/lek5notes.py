# onclick=
document.querySelector('h1')
document.addEventListener('DOMContentLoaded', function()
.innerHTML
.onsubmit
submit.disabled = false;
document.createElement('li')
.append(li)
setInterval(count, 1000);
localStorage.getItem
localStorage.setItem
if (!localStorage.getItem('counter'))
    fetch().then()

document.querySelector('#emails-view').style.display = 'none';
document.querySelector('#compose-view').style.display = 'block';










<script>
    alert('Hello, world!');
</script>

<button onclick="hello()">Click Here</button>

function hello() {
    alert('Hello, world!')
}


let counter = 0;
function count() {
    counter++;
    alert(counter);
}
<button onclick="count()">Count</button>

# !!!! document.querySelector('h1') βρες μου το στοιχείο h1
function() {
    document.querySelector('h1').innerHTML = `Goodbye!`;
}

function hello() {
    const header = document.querySelector('h1');
    if (document.querySelector('h1').innerHTML === 'Hello!') {
        document.querySelector('h1').innerHTML = 'Goodbye!';
    }
    else {
        document.querySelector('h1').innerHTML = 'Hello!';
    }
}

if___() {} else {}
===

οι μεταβλητες μπορούν να σωσουν και html
function hello() {
    let header = document.querySelector('h1');
    if (header.innerHTML === 'Hello!') {
        header.innerHTML = 'Goodbye!';
    }
    else {
        header.innerHTML = 'Hello!';
    }
}
αντι για Let μπορώ με const

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`) #αντι για εισαγωγικα έχει `` που λειτουργούν σαν το f() της python  και $()
    }
}

# δεν καλεί το count() αλλά το count
# δηλαδη λέει μην τρέξεις την συναρτηση ωσπου να πατηθεί το κουμπι
# εδω βλέπουμε ενα παράδειγμα όπου μια εξίσωση σώζετε εντός μιας μεταβλητης (όπως πριν σωσαμε html) functiional programming
document.querySelector('button').onclick = count;

inspect->console για να δω το τερμιναλ της τζαβα
η τζαβα διαβάζει απο πάνω προς τα κάτω. οπότε αν το document.querySelector('button') δεν θα βρει κάτι αν το κουμπί ειναι  παρα κατω. ή βάζεις τον κόδικα παρακάτω ή

document.addEventListener('DOMContentLoaded', function() {
    // Some code here
}); # δυο αργκιουμεντσ τι ειναι το ιβεντ που ψάχνω, σε αυτη την περίπτοση να έχει τελειώσει η φόρτωση της σελίδα. Και δευτερο το όνομα της εξίσωσης (ή να γράψω όλη την εξίσωση εκει)


αν μεταφέρω τον κόδικα σε ένα άλλο αρχειο ____.js
<script src="counter.js"></script>


#<--

<form>
    <input autofocus id="name" placeholder="Name" type="text">
    <input type="submit">
</form>


<script>
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('form').onsubmit = function() { # .querySelector('form') φέρε μου την φορμα, .onsubmit = function() όταν κάνει σαμπμιτ τρέξε αυτη την συνάρτηση. στην προκειμένη γραφει κατευθείαν την συνάρτηση
            const name = document.querySelector('#name').value;
            alert(`Hello, ${name}`);
            # με το .value παίρνω το περιεχόμενο της φόρμας και το σώζω σε μια μεταβλητη με const/let
            # δεν μπορώ να χρησιμοποιήσω το .document.querySelector(input) γιατί στην σελίδα υπάρχουν πολλά input. σαν css 'tag' '#id' '.class'
        };
    });
</script>

# αλλάζω css με js
<script>
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('#red').onclick = function() {
            document.querySelector('#helo').style.color = 'red'; #.style.color άλαξε το σταιλ κολορ
        }
        #και άλλες δυο φορες για τα άλλα δύο χρωμματα αλλά μπορώ και να το κάνω όλο μαζι όπως παρακάτω


        document.querySelectorAll('button').forEach(function(button) { # .querySelectorAll αντί να φέρει το πρώτο τα φαίρνει όλα # προσοχή .forEach
            button.onclick = function() {
                document.querySelector("#hello").style.color = button.dataset.color; # αντί να φωνάξει το κουμπί φώναξε το χελόου.
                # button.dataset.color
            }
    });
    });

<body>
    <h1 id="hello">Hello</h1>
    <button id="red">Red</button>
    <button id="blue">Blue</button>
    <button id="green">Green</button>

    # data tributes
    <button data-color="red">Red</button>
    <button data-color="blue">Blue</button>
    <button data-color="green">Green</button>
</body>


# το ίδιο αλλα με dropdown
<script>
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('select').onchange = function() { #.onchange
            document.querySelector('#hello').style.color = this.value; # this αναφέρετε στο προηγούμενο selector
        }
    });
</script>


# todo list
<form>
    <input id="task" placeholder = "New Task" type="text">
    <input id="submit" type="submit">
</form>


// Wait for page to load
document.addEventListener('DOMContentLoaded', function() {

    // Select the submit button and input to be used later
    const submit = document.querySelector('#submit'); #const/let
    const newTask = document.querySelector('#task');

    // Disable submit button by default:
    submit.disabled = true;

    // Listen for input to be typed into the input field
    newTask.onkeyup = () => {
        if (newTask.value.length > 0) {
            submit.disabled = false;
        }
        else {
            submit.disabled = true;
        }
    }

    // Listen for submission of form
    document.querySelector('form').onsubmit = () => { # αυτό είναι το ίδιο με το αν έγραφα function() {

    # const task = document.querySelector('#task').value;
    # consol.log(task)

    #δημιουργω μια νέα λίστα
    # const li = document.createElement('li');

    # η οποία έχει μέσα το τασκ δηλαδη ότι έγραψε στην φόρμα
    # li innerHTML = task;

    # προσθεσα το νέο μου στοιχειο στο τασκσ
    # document.querySelector('#tasks').append(li);

    # document.querySelector('#task').value = '';
    # to προσθεσα αργότερα για να ξανακάνει ντισειμπλ το κουμπι
    # document.querySeector('#submit').disabled = True;

    # document.querySeector('#submit').disabled = True;
    # document.querySeector('#task').onkeyup = () => {
    #     document.querySeector('#submit').disabled = False;
    # }


    # το ίδιο αλλιώς με ιφ
    # !!!! ayto diabase

    # document.querySeector('#submit').disabled = True;
    # document.querySeector('#task').onkeyup = () => {
    #   if (document.querySeector('#task').value.length > 0) {
    #       document.querySeector('#submit').disabled = False;
    #   } else {
    #        document.querySeector('#submit').disabled = False;
    #   }
    # }

        // Find the task the user just submitted
        const task = newTask.value;

        // Create a list item for the new task and add the task to it
        const li = document.createElement('li');
        li.innerHTML = task;

        // Add new element to our unordered list:
        document.querySelector('#tasks').append(li);

        // Clear out input field:
        newTask.value = '';

        // Disable the submit button again:
        submit.disabled = true;

        // Stop form from submitting # πρεπει να το κάνω αυτό για να μην ξαναφορτώσει η σελίδα στέλνοντας το ποστ
        return false;
    }
});

# intervals  για να τρέχει διαρκός

let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;

    setInterval(count, 1000); # τρέξε το count() καθε 1000μιλισεκόντ = 1 σεκ
});


# lockal storage
# localStorage.getItem
# localStorage.setItem

if (!localStorage.getItem('counter')) { # προσοχή στο ! σημαίνει if not
    localStorage.setItem('counter', 0);
}


// Check if there is already a value in local storage
if (!localStorage.getItem('counter')) {

    // If not, set the counter to 0 in local storage
    localStorage.setItem('counter', 0);
}

function count() {
    // Retrieve counter value from local storage
    let counter = localStorage.getItem('counter');

    // update counter
    counter++;
    document.querySelector('h1').innerHTML = counter;

    // Store counter in local storage
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    // Set heading to the current value inside local storage
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});


# to object είναι σαν το dictionary

let person = {
    first: 'Harry',
    last: 'Potter'
};

person.first
person[first]


# παράδειγμα με api που στέλνει json για συναλαγματική ισοτημία
# fetch(url).then()

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Currency Exchange</title>
        <script src="currency.js"></script>
    </head>
    <body></body>
</html>

document.addEventListener('DOMContentLoaded', function() {
    // Send a GET request to the URL
    fetch('https://api.exchangeratesapi.io/latest?base=USD')
    // Put response into json form
    # tο παρακάτω ειναι συντομευση του¨
    # .then(response => { return responce.json()})
    .then(response => response.json()) # μετέτρεψε το σε json
    .then(data => {
        // Log data to the console
        console.log(data);
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Send a GET request to the URL
    fetch('https://api.exchangeratesapi.io/latest?base=USD')
    // Put response into json form
    .then(response => response.json())
    .then(data => {

        // Get rate from data
        const rate = data.rates.EUR;

        // Display message on the screen
        document.querySelector('body').innerHTML = `1 USD is equal to ${rate.toFixed(3)} EUR.`;
    });
});



<form>
    <input id="currency" placeholder="Currency" type="text">
    <input type="submit" value="Convert">
</form>
<div id="result"></div>

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
                // Display exchange on the screen
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
                // Display error on the screen
                document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.log('Error:', error);
        });
        // Prevent default submission
        return false;
    }
});
