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
}