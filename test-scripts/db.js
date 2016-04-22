var express = require('express');
var router = express.Router();
var mysql = require('mysql');

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.setTimeout(999999);
  // The code below borrowed in part from the NPM MySQL package documentation at:
  // https://www.npmjs.com/package/mysql
  var connection = mysql.createConnection({
    host:'192.168.0.99',
    user:'node',
    password:'secretpass',
    database:'employees'
  });

  res.outNames = [];

  connection.connect();

//  connection.query({sql:'SELECT `last_name`, `first_name`, `salary`, `dept_name` FROM `Departments`, `dept_emp`, `employees`, `salaries` WHERE `salary` = (SELECT MAX(`salary`) FROM `salaries`) AND departments.dept_no = dept_emp.dept_no AND dept_emp.emp_no = employees.emp_no AND employees.emp_no = salaries.emp_no ORDER BY `salary`;',timeout:999999}, function(err, rows, fields) {
//  connection.query({sql:'SELECT `last_name`, `first_name`, `salary` FROM `employees`, `salaries` WHERE `salary` = (SELECT MAX(`salary`) FROM `salaries`) AND employees.emp_no = salaries.emp_no;',timeout:999999}, function(err, rows, fields) {
  connection.query({sql:'SELECT last_name FROM `employees` WHERE first_name = "Steve" LIMIT 3;',timeout:999999}, function(err, rows, fields) {
    if (err) {
      var output = "error! " + err;
      console.log(output);
      res.send(output);
    }
    else {
      for (item of rows) {
        res.outNames.push(item["last_name"]);
        if(res.outNames.length >= 6) {
          var output = "";
          for (item of res.outNames) {
            output += item + "<br>";
          }
          res.send(output);
        }
      }
      //res.send(output);
    }
  });

  connection.query({sql:'SELECT last_name FROM `employees` WHERE first_name = "Tran" LIMIT 3;',timeout:999999}, function(err, rows, fields) {
    if (err) {
      var output = "error! " + err;
      console.log(output);
      res.send(output);
    }
    else {
      for (item of rows) {
        res.outNames.push(item["last_name"]);
        if(res.outNames.length >= 6) {
          var output = "";
          for (item of res.outNames) {
            output += item + "<br>";
          }
          res.send(output);
        }
      }
      //res.send(output);
    }
  });

  connection.end();
});

module.exports = router;
