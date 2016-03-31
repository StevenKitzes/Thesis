var express = require('express');
var router = express.Router();
var mysql = require('mysql');

/* GET users listing. */
router.get('/', function(req, res, next) {
  // The code below borrowed in part from the NPM MySQL package documentation at:
  // https://www.npmjs.com/package/mysql
  var connection = mysql.createConnection({
    host:'192.168.0.99',
    user:'node',
    password:'secretpass',
    database:'employees'
  });

  connection.connect();

  connection.query('SELECT * from `departments`', function(err, rows, fields) {
    if (err) {
      res.send("error! " + err);
    }

    res.send("first dept number: " + JSON.stringify(rows[0]));
  });

  connection.end();
});

module.exports = router;
