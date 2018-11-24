

const ul = document.getElementById("notes-list");

const url = '/notes';

fetch(url)
    .then(function(data) {
        console.log(data);

        let notesList = data.results;
        return notesList.map((topic) => {
            let li = createNode('li');
            append(ul, li);

        })
    })


function createNode(element) {
    return document.createElement(element);
}

function append(parent, el) {
    return parent.appendChild(el);
}