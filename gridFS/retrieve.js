let mongoose = require('mongoose')

mongoose.connect('mongodb://nfusion:18ZcdsEZ4weVdlIJqTf7seA5gI2hjRSab8U9bp2EOxnMFugRrvHNBh6UNsxe29DsSOXOTsp8nQwW7IXZtLvviA%3D%3D@nfusion.documents.azure.com:10255/?ssl=true')
let db = mongoose.connection
db.on('error', console.error.bind(console, 'connection error:'))
db.once('open', function() {
  // we're connected!
})
