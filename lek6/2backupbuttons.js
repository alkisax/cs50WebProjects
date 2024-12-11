document.addEventListener('DOMContentLoaded', function() {
    // Check if the new post div exists before initializing its animation
    const newPostDiv = document.getElementById('newpost');
    if (newPostDiv) {
        initNewPostAnimation();
    }

    // Check if the toggle button exists before initializing it
    const toggleButton = document.getElementById('toggle-newpost');
    if (toggleButton) {
        initToggleButton();
    }

    //initEditButton();

});

/*
function initEditButton() {
    const editButtons = document.querySelectorAll('[id^="editbutton-"]');
    const editPost = document.getElementById('editpost');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const postId = button.getAttribute('data-post-id');
            const postBox = document.getElementById(`post-box-${postId}`);
            postBox.innerHTML = editPost.innerHTML;

            const initialTitle = document.getElementById(`posttitle-${postId}`);
            const parsedInitialContent = document.querySelectorAll(`#postcontent-${postId} ~ p`);
            let contentText = '';

            parsedInitialContent.forEach(function(p) {
                contentText += p.innerText + '\n';
            });
            const titleText = initialTitle.innerText;

            document.querySelector('#newtitle').value = titleText;
            document.querySelector('#newcontent').value = contentText;
            document.querySelector('#newtitle').focus();

            const postBox = document.getElementById(`post-box-${postId}`);
            postBox.innerHTML = editPost.innerHTML;

            const editForm = postBox.querySelector('form');
            editForm.setAttribute('data-post-id', postId);
            document.querySelector('#newtitle').focus();

            document.querySelector('#submiteditbutton').addEventListener('click', function(event) {
                event.preventDefault();
                const newtitle = document.querySelector('#newtitle').value;
                const newcontent = document.querySelector('#newcontent').value;

                fetch(`/index/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify({
                        post_id: postId,
                        title: newtitle,
                        content: newcontent
                    })
                })
                .then(response => {
                    if (response.ok) {
                        console.log('Post updated successfully!');
                        location.reload();
                    } else {
                        console.error('Error updating post:', response.statusText);
                    }
                })
                .catch(error => {
                    console.error("Fetch error:", error);
                });
            });

        });
    });
}
*/

/*
my psuedocode is
get button in constant
get post-box in constant
get editpost in constant
add .onclick to button
then toggle the view of post-box
retrieve post-box info
populate editpost
toggle the view of editpost
*/


/*
ok so now we have created a constant that catches all the buttons
a constant tha cachest the container (the placeholder for the edit form
a constant for for the edit form
next we set an alarm for every button to see which one will be clicked and if it happens we prevent its normal behavior (submit)
*/

/*
function initEditButton() {
    const editButtons = document.querySelectorAll('[id^="editbutton-"]');
    // II const editContainer = document.getElementById('editcontainer');
    const editPost = document.getElementById('editpost');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            //II
            const postId = button.getAttribute('data-post-id');
            const postBox = document.getElementById(`post-box-${postId}`);

             next i want to take the innerHtml from my template aka editPost and give it to the editContainer

            // ME ΛΑΤΙΝΙΚΗ ΑΡΗΘΜΗΣΗ ΟΙ ΑΛΛΑΓΕΣ ΠΟΥ ΕΓΙΝΑΝ ΓΙΑΝ ΝΑ ΕΜΦΑΝΙΖΕΤΕ ΣΤΟ POSTBOX KAI OXI STO EDITCONTAINER

            // I editContainer.innerHTML = ''; // Clear previous
            // I editContainer.innerHTML = editPost.innerHTML;
            postBox.innerHTML = editPost.innerHTML;

/*
            now the next steps
            1. retrieve the title and the content of the post (that the button wa pressed) and save them in constants
            2. populate the new form with them

            lets go to 1.
            lets keep in mind that in every post while looping we added an id like:
            id="posttitle-{{ post.id }}"
            id="postcontent-{{ post.id }}"
            and this are shown in box named
            post-box-{{ post.id }}
            but first we need to retrieve the post id
*/

/*
            εδω βαζω ένα απλο παραδειγμα του τι κάνει το .getAttribute:
            <button id="myButton" data-info="123">Click me</button>
            const button = document.getElementById('myButton');
            const info = button.getAttribute('data-info');
            console.log(info); // This will output: 123
            απθηκευω εναλακτικές κρυφές πληροφορίες. Στην περιπτωση μου το id του Post
*/

            // II const postId = button.getAttribute('data-post-id');

/* (για καποιο λογο δεν εκανε κομεντ αουτ και προσθεσα αυτο)

            const initialTitle = document.getElementById(`posttitle-${postId}`);
            //debuging μου τύπωνε μόνο τον τιτλο και οχι το σωμα του ποστ. Επειεδη το linebreak μου φτιάχενει παραγράφους με πολλαπλά <p> πρεπει να προσέξω να μην πάρω μόνο το πρωτο. για αυτό η αλλαγή.
            //const initialContent = document.getElementById(`postcontent-${postId}`);


            // παιρνω και όλα τα child <p>
            const parsedInitialContent = document.querySelectorAll(`#postcontent-${postId} ~ p`);

            let contentText  = '';

            parsedInitialContent.forEach(function(p) { // δεν μου αρεσε αλλα θα μπορούσε p => // το .forEach πρακτικα λειτουργει σαν for loop

                contentText  += p.innerText + '\n';
            });
            //Now, to get the actual text inside those elements
            const titleText = initialTitle.innerText;
            //debuging. επειδη λόγο του debuging το ευτιαξα αλλιώς παρπανω το σβήνω απο εδω
            //const contentText = initialContent.innerText;

            //step 2  populate the new form, we have to titleText and contentText. in html the αντιστοιχα ονοματα sto editpost είναι id="newtitle" kai id="newcontent"

            document.querySelector('#newtitle').value = titleText;
            document.querySelector('#newcontent').value = contentText;

            // II
            // Show the edit form
            document.querySelector('#newtitle').focus();

/* III
            if (editContainer.style.display === 'none' || editContainer.style.display === '') {
                editContainer.style.display = 'block';
                // αν εβαζα απλως autofocus στο title δεν θα δουλευε γιατι η σελιδα δεν κανει ριφρεσ καθε φορα που πατιέτε το κουμπι
                document.querySelector('#newtitle').focus();
            } else {
                editContainer.style.display = 'none';
            }
*/

/* (για καποιο λογο δεν εκανε κομεντ αουτ και προσθεσα αυτο)

            // III
            // III Replace the contents of the post-box with the edit form
            const postBox = document.getElementById(`post-box-${postId}`);
            postBox.innerHTML = editPost.innerHTML;

            // III Add the necessary ID to the edit form
            const editForm = postBox.querySelector('form');
            editForm.setAttribute('data-post-id', postId);

            // III Optionally, focus on the title input
            document.querySelector('#newtitle').focus();


            // Απο εδω και κάτω συνχονεύω το κουμπι submit edit γιατι δεν μου έσωζε το κείμενο που του έβαζα. Ο λόγος ήταν οτι επρεπε να ξαναγίνει Populated και να μπει το event listener γιατι εκανε ριφρεσ πριν κανει φετσ
            // *** PART II ***
/* PSUEDOCODE
                there is a button called submit edit
                we will create a new js fuction that is runned when clicked
                here is my initial psuedocode

                1. add the button to an const:
                <button type="submit" id="submiteditbutton" class="submit-btn" data-post-id="{{ post.id }}">Submit Edit</button>

                2. add eventlistener on button for click
                3. prevent from submiting event
                4. get post id
                5. retreave content and title and save them to const. id="newtitle" id="newcontent"
                6. create a fetch put to send to jango
                7. optimise jango for updating the models
                8. update the parts to be refreshed without refreshing the page
*/
            // 2

/* (για καποιο λογο δεν εκανε κομεντ αουτ και προσθεσα αυτο)

            // **Reattach the event listener to the newly populated submit button**
            document.querySelector('#submiteditbutton').addEventListener('click', function(event) {
                event.preventDefault();
                console.log("Submit Edit button clicked!");

                // Get new title and content
                //5. create a fetch put to send to jango προσοχη στο .value
                const newtitle = document.querySelector('#newtitle').value;
                const newcontent = document.querySelector('#newcontent').value;

                //6. create a fetch put to send to jango
                // Send PUT request to update post
                fetch(`/index/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify({
                        post_id: postId,
                        title: newtitle,
                        content: newcontent
                    })
                })
                // added for debug
                .then(response => {
                    if (response.ok) {
                        console.log('Post updated successfully!');
                        location.reload(); // Refresh the page to see the changes
                    } else {
                        console.error('Error updating post:', response.statusText);
                    }
                })
                .catch(error => {
                    console.error("Fetch error:", error);
                });
            });

        });
    });
}
*/


function initToggleButton() {
    // για να κάνω toggle με κουμπί το new post κουτι //
    const toggleButton = document.getElementById('toggle-newpost');
    const newPostDiv = document.getElementById('newpost');

    toggleButton.onclick = function(){
        if (newPostDiv.style.display === 'none' || newPostDiv.style.display === '') {
            newPostDiv.style.display = 'block';
            newPostDiv.style.animationPlayState = 'running'; //τελικά αναγκάστικα να τις μπλέξω τις δύο συναρτήσεις
        } else {
            newPostDiv.style.animationPlayState = 'paused'; //τελικά αναγκάστικα να τις μπλέξω τις δύο συναρτήσεις
            newPostDiv.style.display = 'none';
        }
    };
}


// πότε να ενεργοποιήτε το animation του new post //
//document.addEventListener('DOMContentLoaded', function() {
function initNewPostAnimation() {
    const newPostDiv = document.getElementById('newpost');
    newPostDiv.style.animationPlayState = 'paused'; // Start with animation paused
    newPostDiv.style.display = 'none'; // Ensure it's hidden initially
}






/* //εδω φτιάχνω τις συναρτησεις μου για infinite scroll με 5 ποστ την φορα

let start = 0; // Starting index for posts
const loadCount = 5;

window.onscroll = () => {
    // Check if the user has scrolled to the bottom of the page
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load(); //αν το βάλω να τρέχει αυτόματα κάθε φορά που φτανει στο τελος έχω infinite scroll
    }
};

function load() {

    const end = start + loadCount;

    fetch(`/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            if (data.posts.length > 0) {
                data.posts.forEach(add_post);
                start += loadCount;
        }
    })
}; */



