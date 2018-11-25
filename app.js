let {PythonShell} = require('python-shell')
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
        let pathToTopics = path.join(pathToFiles, `${dir[i]}/notes.txt`) 
        console.log(pathToTopics)
        notes.title.push(dir[i])
        notes.content.push(fs.readFileSync(pathToTopics, 'utf8'))
    }
    res.json(notes)
})

app.post('/upload-note', (req, res) => {
    //console.log(req.body.topic)
    
    if (Object.keys(req.files).length == 0) {
        return res.status(400).send('No files were uploaded.');
      }
      // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
      let sampleFile = req.files.file;
      // Use the mv() method to place the file somewhere on your server
      pathToSave = path.join(__dirname, '/back/new_notes.txt')
      sampleFile.mv(pathToSave, function(err) {
        if (err)
          return res.status(500).send(err);
        console.log('File uploaded', fileId)
    });

    // let options = {
    //     args: [`${req.body.topic}`]
    // };

    // PythonShell.run('back/compiler.py', options, function(err, results) {
    //     if(err) throw err;
    // })
    // res.end();
    })
app.get('/topics', (req, res) => {
    res.json(dir)
})

app.listen(3000);

/* 
1. Select topic
    - check against current ones
    - if not in current topics - add new
2. Python call - > Saves a file in writeTo
*/