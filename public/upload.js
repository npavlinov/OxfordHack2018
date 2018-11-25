const selects = document.querySelector('#inputGroupSelect01')
const topic_url = '/topics';

getTopics()

function getTopics() {
    fetch(topic_url)
    .then(response => response.json())
    .then(topics => {
        topics.forEach(topic => {
            let option = document.createElement('option')
            option.text = topic
            option.value = topic
            selects.appendChild(option)
        });
    })
    .then(() => {
        let optionAdd = document.createElement('option')
        optionAdd.text = 'Add a course'
        optionAdd.value = 'add'
        selects.appendChild(optionAdd)
    })
}

function addCourse(that) {
    if(that.value == 'add') {
        document.getElementById('ifAdd').style.display = "block"
        document.getElementById('inputGroupSelect01').name = ""
    } else {
        document.getElementById('ifAdd').style.display = "none"   
        document.getElementById('inputGroupSelect01').name = "topic"

    }
}