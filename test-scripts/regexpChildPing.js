var express = require('express');
var router = express.Router();
var child_process = require('child_process');

/* GET users listing. */
router.get('/', function(req, res, next) {
  child_process.exec('sleep 5; echo "slept 5"', function (err, stdout, stderr){
    if (err) {
      console.log("child processes failed with error code: " +
      err.code);
    }
    res.send(stdout);
  });
});

module.exports = router;