document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // By default, load the inbox
    load_mailbox('inbox');
  });

  function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';

    // post an email //prepei na balo csrf
    document.querySelector('form').onsubmit = function() {
      const recipients = document.querySelector('#compose-recipients').value;
      const subject = document.querySelector('#compose-subject').value;
      const body = document.querySelector('#compose-body').value;

      fetch('/emails', {
        method: 'POST',
        body: JSON.stringify({
            recipients: recipients,
            subject: subject,
            body: body,
            read: false // Set the read status to false when sending
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
          console.log(result);
          // Load the sent mailbox after sending
          load_mailbox('sent');
      });

      // Prevent default form submission
      return false;
    };
  }

  function load_mailbox(mailbox) {

    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    // You’ll likely want to make a GET request to /emails/<mailbox> to request the emails for a particular mailbox.
    // When a mailbox is visited, the application should first query the API for the latest emails in that mailbox.

    fetch(`/emails/${mailbox}`) // Use mailbox variable
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);
        if (emails.length === 0) {
          document.querySelector('#emails-view').innerHTML += '<p>No emails found</p>';
        }

        // Loop through each email
        emails.forEach(email => {
          console.log(email);
          const id = email.id;
          const sender = email.sender;
          const recipients = email.recipients;
          const subject = email.subject;
          const body = email.body;
          const timestamp = email.timestamp;
          const read = email.read;
          const archived = email.archived;

        //Each email should then be rendered in its own box (e.g. as a <div> with a border) that displays who the email is from, what the subject line is, and the timestamp of the email.
        // const container = document.createElement('div');
        const maillistitem = document.createElement('div');

        maillistitem.style.border = '1px solid black';
        maillistitem.style.padding = '10px';
        maillistitem.style.borderRadius = '5px';
        maillistitem.style.margin = '10px 0';

        if (read === true) {
          maillistitem.style.background = 'grey'
        } else {
          maillistitem.style.background = 'white'
        }

        maillistitem.innerHTML = `
            <strong>From: </strong>${sender}<br>
            <strong>Subject: </strong>${subject}<br>
            <strong>${timestamp}</strong><br>
            <p>Status: ${archived}</p>
            `;

        //const button = document.createElement('button');
        //button.textContent = 'Button';
        // maillistitem.append(button);

        //button.addEventListener('click', function(event) {
        //  console.log('Button clicked');
        //});
        const container = document.createElement('div');
        container.append(maillistitem);

        console.log(mailbox);
        if (mailbox === 'inbox') {
          console.log('Creating button');
          const button = document.createElement('button');
          button.textContent = 'Archive';
          button.addEventListener('click', function(event) {
            console.log('Button clicked');
            archive(id);
          });
          container.append(button);
        }
        else if (mailbox === 'archive') {
          console.log('Creating button');
          const button = document.createElement('button');
          button.textContent = 'Unarchive';
          button.addEventListener('click', function(event) {
            console.log('Button clicked');
            unarchive(id);
          });
          container.append(button);
        }

        document.querySelector('#emails-view').append(container);

        maillistitem.addEventListener('click', function () {
          console.log('email has been clicked');
          open_email(id, maillistitem); // πρεπει να περαστει και το maillistitem ωστε να περαστούνμέσα του και οι αλλαγές πουθα γίνειστο οπεν (συγγεκριμενα να καταχωρηθεί ως διαβασμένο)
        });
      });
    });
  }

  function open_email(id, maillistitem) {

    maillistitem.style.background = 'white'; //περασα και το Maillistitem εδω

    fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
        // Print email
        console.log(email);
        // Log the read status before updating
        console.log('Before marking as read:', email.read);

        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        })
        .then(function () {
          console.log('Email marked as read');

          // Clear any previous content in '#emails-view'
          document.querySelector('#emails-view').innerHTML = '';

          // Your application should show the email’s sender, recipients, subject, timestamp, and body.
          const sender = email.sender;
          const recipients = email.recipients;
          const subject = email.subject;
          const body = email.body;
          const timestamp = email.timestamp;
          let read = email.read;
          const archived = email.archived;

          const mailitem = document.createElement('div');
          mailitem.innerHTML = `
            <strong>From: </strong>${sender}<br>
            <strong>Subject: </strong>${subject}<br>
            <strong>recipients: </strong>${recipients}<br>
            <strong>${timestamp}</strong><br>
            <p>${body}</p>
          `;

          document.querySelector('#emails-view').append(mailitem);

          //const container = document.createElement('div');
          const button = document.createElement('button');
          if (archived === false) {
            button.textContent = 'Archive';
            button.addEventListener('click', function(event) {
              console.log('Button clicked');
              archive(id);
            });
          } else {
            button.textContent = 'Unarchive';
            button.addEventListener('click', function(event) {
              console.log('Button clicked');
              unarchive(id);
            });
          }
          //container.append(button);
          document.querySelector('#emails-view').append(button);

          const replybutton = document.createElement('button');
          // replybutton.style.padding = '10px';
          replybutton.style.marginTop = '10px';
          replybutton.textContent = 'Reply';
          replybutton.addEventListener('click', function(event) {
            console.log('Button clicked');
            reply(id);
            });
          document.querySelector('#emails-view').append(replybutton);
        });
    });
  }


  function archive(id) {

    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
          archived: true
      })
    })
    .then (function () {
      console.log('email archived');
      load_mailbox('inbox');
    });
  }


  function unarchive(id) {

    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
          archived: false
      })
    })
    .then (function () {
      console.log('email unarchived');
      load_mailbox('inbox');
    });
  }


  function reply(id) {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
          const sender = email.sender;
          const recipients = email.recipients;
          const subject = email.subject;
          const body = email.body;
          const timestamp = email.timestamp;

      // Clear out composition fields
      document.querySelector('#compose-recipients').value = sender;

      if (subject.startsWith("Re:")) {
        document.querySelector('#compose-subject').value = subject;
      } else {
        document.querySelector('#compose-subject').value = `Re: ${subject}`;
      }
      document.querySelector('#compose-body').value = `on ${timestamp} ${sender} wrote: \n${body}`;

      // post an email //prepei na balo csrf
      document.querySelector('form').onsubmit = function() {
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;

        fetch('/emails', {
          method: 'POST',
          body: JSON.stringify({
              recipients: recipients,
              subject: subject,
              body: body
          })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            // Load the sent mailbox after sending
            load_mailbox('sent');
        });

        // Prevent default form submission
        return false;
      };
    });
  }
