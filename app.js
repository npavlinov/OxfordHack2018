const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.use(express.static('public'));

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
    res.json("hello");
})


app.listen(3000);
