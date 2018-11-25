const ul = document.querySelector('#notes-list');
const notesHTML = document.querySelector('#notes-list-content')
const selects = document.querySelector('#inputGroupSelect01')
const url = '/notes';
const topic_url = '/topics';

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
            let li = document.createElement('li')
            li.classList.add("alert")
            li.classList.add("alert-primary")
            //assign them
            h1.textContent = notes.title[i]
            li.textContent = notes.content[i]
            console.log(h1, li)
            //append them
            div.appendChild(h1)
            div.appendChild(li)
            div.appendChild(hr)
            notesHTML.appendChild(div)
        }
    })
}

getTopics()

function getTopics() {
    fetch(topic_url)
    .then(response => response.json())
    .then(topics => {
        console.log(topics)
        topics.forEach(topic => {
            console.log(topic)
            let option = document.createElement('option')
            option.text = topic
            option.value = topic.toLowerCase()
            selects.appendChild(option)
        });
    })
}