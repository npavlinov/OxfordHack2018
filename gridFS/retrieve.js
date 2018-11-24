let mongoose = require('mongoose');
let Schema = mongoose.Schema;
let fs = require('fs');
let path = require('path');
let Grid = require('gridfs-stream');

mongoose.connect('mongodb://nfusion:18ZcdsEZ4weVdlIJqTf7seA5gI2hjRSab8U9bp2EOxnMFugRrvHNBh6UNsxe29DsSOXOTsp8nQwW7IXZtLvviA%3D%3D@nfusion.documents.azure.com:10255/?ssl=true')
let conn = mongoose.connection

Grid.mongo = mongoose.mongo;


conn.once('open', function() {
    // we're connected!
    console.log('DB onnection open');
    let gfs = Grid(conn.db);

    let filename = "sample.txt";
    // write content from DB to filesystem
    let fs_write_stream = fs.createWriteStream(path.join(__dirname, `../writeTo/${filename}`));

    // create read stream from mongoDB
    let read_stream = gfs.createReadStream({
      filename: 'sample.txt'
    })

    read_stream.pipe(fs_write_stream);
    fs_write_stream.on('close', function () {
      console.log('File has been written fully');
    });
})

conn.on('error', console.error.bind(console, 'connection error:'))


