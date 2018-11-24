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


function onFileReceive() {
    let input = document.getElementById('uploadNotes');

    for (var i = 0; i < input.files.length; i++) {
        console.log("input: %O",input);
        console.log("input: %O",input.files);
    }
}