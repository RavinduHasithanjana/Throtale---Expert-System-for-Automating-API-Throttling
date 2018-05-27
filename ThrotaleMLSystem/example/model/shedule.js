var mongoose = require('mongoose');


mongoose.connect('mongodb://test:12345@ds247327.mlab.com:47327/getfit');

var Schema = mongoose.Schema;

var fitnessschema = new mongoose.Schema({
  
}, { collection : 'Shedule' });

module.exports = mongoose.model('Shedule',fitnessschema);