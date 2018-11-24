const express = require('express');
const app = express();
const path = require('path')
const fs = require('fs')
const cors = require('cors')
const fileUpload = require('express-fileupload')

app.use(fileUpload())
app.use(cors())
app.set('view engine', 'ejs');
app.use(express.static('public'));

let fileId = 0;
let notes = {
    'title': [],
    'content': []
}

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
app.get('/notes', (req, res) => {
    notes = {
        'title': [],
        'content': []
    }
    for(let i = 0; i < dir.length; i++) {
        let pathToFile = path.join(__dirname, `/writeTo/${dir[i]}`)
        notes.title.push(dir[i])
        notes.content.push(fs.readFileSync(pathToFile, 'utf8'))
        // notes.content.push(fs.readFileSync(pathToFile, 'utf8'))
    }
    res.json(notes)
})

app.post('/upload-note', (req, res) => {
    if (Object.keys(req.files).length == 0) {
        return res.status(400).send('No files were uploaded.');
      }
      // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
      let sampleFile = req.files.file;
      // Use the mv() method to place the file somewhere on your server
      pathToSave = path.join(__dirname, `/writeTo/${fileId++}.txt`)
      sampleFile.mv(pathToSave, function(err) {
        if (err)
          return res.status(500).send(err);
        console.log('File uploaded', fileId)
      });
})
app.listen(3000);
