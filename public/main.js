const ul = document.querySelector('#notes-list');
const url = '/notes';

listAllNotes();

function listAllNotes() {
    ul.innerHTML = '';  
    fetch(url)
    .then(response => response.json())
    .then(notes => {
        notes.forEach(note => {
            let li = document.createElement('li');
            li.textContent = note;

            ul.appendChild(li);
        })
    })
}