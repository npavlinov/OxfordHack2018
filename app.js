const express = require('express');
const app = express();
const path = require('path')
const fs = require('fs')
const cors = require('cors')

app.use(cors())
app.set('view engine', 'ejs');
app.use(express.static('public'));

let notes = []

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/download', (req, res) => {
    res.render('download');
});

app.get('/upload', (req, res) => {
    res.render('upload');
});

app.get('/notes', (req, res) => {
    for(let i = 0; i < dir.length; i++) {
        let pathToFile = path.join(__dirname, `/writeTo/${dir[i]}`)
        let readStream = fs.createReadStream(pathToFile)
        notes.push(fs.readFileSync(pathToFile, 'utf8'))
    }
    res.json(notes)
})

app.listen(3000);
