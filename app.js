const express = require('express')
let mongoose = require('mongoose')
const app = express()

mongoose.connect('mongodb://localhost/test')
let db = mongoose.connection
db.on('error', console.error.bind(console, 'connection error:'))
db.once('open', function() {
  // we're connected!
})

var kittySchema = new mongoose.Schema({
    name: String
  });

var Kitten = mongoose.model('Kitten', kittySchema);

var silence = new Kitten({ name: 'Silence' });
console.log(silence.name); // 'Silence'

// NOTE: methods must be added to the schema before compiling it with mongoose.model()
kittySchema.methods.speak = function () {
    var greeting = this.name
      ? "Meow name is " + this.name
      : "I don't have a name";
    console.log(greeting);
  }
  
var Kitten = mongoose.model('Kitten', kittySchema);

fluffy.save(function (err, fluffy) {
    if (err) return console.error(err);
    fluffy.speak();
  });

app.set('view engine', 'ejs');
app.use(express.static('public'))
app.get('/', (req, res) => {
    res.render('index')
}).listen(3000)


// mongodb://nfusion:18ZcdsEZ4weVdlIJqTf7seA5gI2hjRSab8U9bp2EOxnMFugRrvHNBh6UNsxe29DsSOXOTsp8nQwW7IXZtLvviA%3D%3D@nfusion.documents.azure.com:10255/?ssl=true