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

let pathToFiles = path.join(__dirname, '/writeTo/')
let dir = fs.readdirSync(pathToFiles)
// let pathToFile = path.join(__dirname, `/writeTo/${dir[1]}`)
// fs.readFile(pathToFile, 'utf8', (err, data) => {
//     console.log(data)
// })
// console.log(readStream.pipe())
// console.log(dir[1])
// console.log(allFiles)
app.get('/notes', (req, res) => {
    for(let i = 0; i < dir.length; i++) {
        let pathToFile = path.join(__dirname, `/writeTo/${dir[i]}`)
        let readStream = fs.createReadStream(pathToFile)
        notes.push(fs.readFileSync(pathToFile, 'utf8'))
    }
    res.json(notes)
})
    // let readStream = fs.createReadStream(pathToFiles)


app.listen(3000);
