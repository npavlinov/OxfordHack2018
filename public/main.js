const ul = document.getElementById('notes-list');
const url = '/notes';

ul.empty();

fetch(url)
    .then(response => response.json())
    .then(notes => {
        ul.innerHTML = ''
        notes.forEach(note => {
            const li = document.createElement('li');
            li.textContent = note;
            ul.appendChild(li);
        })
    
    })