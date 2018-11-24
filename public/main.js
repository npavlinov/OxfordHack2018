const ul = document.querySelector('#notes-list');
const notesHTML = document.querySelector('#notes-list-content')
const url = '/notes';

listAllNotes();

function listAllNotes() {
    ul.innerHTML = '';  
    fetch(url)
    .then(response => response.json())
    .then(notes => {
        for(let i = 0; i < notes.title.length; i++) {
            let div = document.createElement('div')
            //create the title and the content
            let h1 = document.createElement('h1')
            let li = document.createElement('li')
            //assign them
            h1.textContent = notes.title[i]
            li.textContent = notes.content[i]
            console.log(h1, li)
            //append them
            div.appendChild(h1)
            div.appendChild(li)
            notesHTML.appendChild(div)
        }
    })
}


function onFileReceive() {
    let input = document.getElementById('uploadNotes');

    for (var i = 0; i < input.files.length; i++) {
        console.log("input: %O",input);
        console.log("input: %O",input.files);
    }
}