let mongoose = require('mongoose')
let Schema = mongoose.Schema
//establish connection
mongoose.connect('mongodb://nfusion:18ZcdsEZ4weVdlIJqTf7seA5gI2hjRSab8U9bp2EOxnMFugRrvHNBh6UNsxe29DsSOXOTsp8nQwW7IXZtLvviA%3D%3D@nfusion.documents.azure.com:10255/?ssl=true')
let conn = mongoose.connection
let path = require('path')
//connect to gridFS
let Grid = require('gridfs-stream')
//require fs 
let fs = require('fs')

//get file path
let videoPath = path.join(__dirname, "../readFrom/text.txt")

//connect grid to mongo
Grid.mongo = mongoose.mongo

conn.once('open', function() {
  console.log('Connection established!')
  let gfs = Grid(conn.db)

  //when db connects create write stream with the name
  //to store file in db
  let writeStream = gfs.createWriteStream({
    filename: 'sample.txt'
  })

  // create read stream from where the video is atm and pipe it 
  // to the db using writestream
  fs.createReadStream(videoPath).pipe(writeStream)

  writeStream.on('close', (file) => {
    console.log(file.filename + ' written to DB')
  })
})

