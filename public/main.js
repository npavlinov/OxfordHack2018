const ul = document.getElementById('notes-list');
const url = '/notes';

fetch(url)
    .then(response => response.json())
    .then(notes => {
        notes.forEach(note => {
            const li = document.createElement('li');
            li.textContent = note;
            ul.appendChild(li);
        });
    })