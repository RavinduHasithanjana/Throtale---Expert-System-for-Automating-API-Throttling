var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var shedule = require("./model/shedule");
var mongo = require('mongodb').MongoClient;
var morgan = require('morgan');
var path = require('path');
var fs = require('fs');
var cron = require('node-cron');
var spawn = require('child_process').spawn;
py    = spawn('python', ['test.py',"hlls"]);
data = [1,2,3,4,5,6,7,8,9];
var PythonShell = require('python-shell');
const axios = require('axios');



app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 5000;
var accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {flags: 'a'})

// setup the logger
app.use(morgan('combined', {stream: accessLogStream}))

// call the python.script
var PythonShell = require('python-shell');

// PythonShell.run('../Throtale.py', function (err) {
//   if (err) throw err;
//   console.log('finished');
// });


py = spawn('python', ['../Throtale.py',"hlls","mills"])
py.stdout.on('data', function(data){
  console.log(data.toString());

});


// writing the corn job
cron.schedule('* * * * * *', function(){

  axios.get('http://0.0.0.0:5000/')
    .then(response => {
  //     console.log(data);
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });

});


var router = express.Router();

router.get('/all', function(req, res) {  // connection to the shedule collection and retrive all the shedules
	console.log(req);
       var response = {};
        shedule.find({},function(err,data){
            if(err) {
                response = {"error" : true,"message" : "Error fetching data"};
            } else {
                response = {"error" : false,"message" : data};
            }
            res.json(response);
        });
});

app.use('/api', router);

app.listen(port);
console.log('Magic happens on port ' + port);
