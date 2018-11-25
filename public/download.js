const ul = document.querySelector('#notes-list');
const notesHTML = document.querySelector('#notes-list-content')
const url = '/notes';

listAllNotes();

function listAllNotes() {
    fetch(url)
    .then(response => response.json())
    .then(notes => {
        for(let i = 0; i < notes.title.length; i++) {
            let div = document.createElement('div')
            let hr = document.createElement('hr')
            //create the title and the content
            let h1 = document.createElement('h1')
            let btn = document.createElement('input');
            btn.setAttribute('type','button');
            btn.classList.add('btn');
            btn.classList.add('btn-primary')
            btn.value = "Download";
            let content = notes.content[i]

            btn.onclick = function() { // Note this is a function
                // alert(content);
                var element = document.createElement('a');
                element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(content));
                element.setAttribute('download', "notes.md");
  
                element.style.display = 'none';
                document.body.appendChild(element);
  
                element.click();
  
                document.body.removeChild(element);
              };

            //assign them
            h1.textContent = notes.title[i]
            //append them
            div.appendChild(h1)
            div.appendChild(btn)
            div.appendChild(hr)
            notesHTML.appendChild(div)
        }
    })
}