var express = require('express');
var router = express.Router();

var Worker = require('webworker-threads').Worker;

var workerOutput = "";

router.get('/', function(req, res, next) {
    console.log("got request");
    // You may also pass in a function: 
    var worker = new Worker(function(){
        this.onmessage = function(event) {
            var bigString = "hello they thee thine hello!";
            console.log("doing string search");
            var output = "";
            console.log("finished a part1");
            output += /\w*(?=\sbetray\sthe\sfore)/.exec(bigString) + "<br>";
            console.log("finished a part2");
            output += /\w*(?=\sspongy\slungs\sbestowed)/.exec(bigString) + "<br>";
            console.log("finished a part3");
            output += /\w*(?=\sjson\sobject\snotation)/.exec(bigString) + "<br>";
            console.log("finished a part4");
            output += /\w*(?=\sshould\sdo\sagain\sfor\ssuch\sa\ssake)/.exec(bigString) + "<br>";
            console.log("finished a part5");
            output += /\w*(?=\sthat\sfalse\sfire)/.exec(bigString) + "<br>";
            console.log("finished a part6");
            output += /\w*(?=\sforced\sthunder\sfrom\shis\sheart)/.exec(bigString) + "<br>";
            console.log("finished a part7");
            output += "found " + bigString.match(/\w*(?=\sthy)/g).length + " words preceding 'thy'<br>";
            console.log("finished a part8");
            output += "found " + bigString.match(/\w*(?=\sthee)/g).length + " words preceding 'thee'<br>";
            console.log("finished a part9");
            output += "found " + bigString.match(/\w*(?=\sthine)/g).length + " words preceding 'thine'<br>";
            console.log("string search done");
            postMessage(output);
            console.log("message posted");
            self.close();
        };
    });
    console.log("defined worker")
    worker.onmessage = function(event) {
        console.log("trying to res data");
        res.send(event.data);
        console.log("tried to res data");
    };
    console.log("defined worker event handler");
    worker.postMessage('start');
    console.log("sent message");
});

module.exports = router;