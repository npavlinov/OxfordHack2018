const ul = document.getElementById('notes-list');
const url = '/notes';

fetch(url)
    .then(response => response.json())
    .then(notes => {
        const li = document.createElement('li');
        li.textContent = notes;
        ul.appendChild(li);
    })