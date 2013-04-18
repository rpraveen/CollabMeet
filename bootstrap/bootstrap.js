var http = require('http');
var sys  = require('sys');
var url = require('url');
var fs = require('fs');

var meetingTable = {};
fs.readFile('files/meetings', 'utf8', function (err,data) {
  if (err) {
    return console.log("Meeting table file not present. File will be created on insert!\n");
  }
  
  meetingTable = JSON.parse(data);
  console.log("Meeting table loaded from persistent storage:\n", meetingTable, "\n");
});

http.createServer(function (request, response) {
  sys.log(request.connection.remoteAddress + ": " + request.method + " " + request.url);

  /* Parse the URL */
  var urlParts = url.parse(request.url, true);
  var query = urlParts.query;
  
  /* Prepare the response */
  response.writeHead(200, {'Content-Type': 'text/plain'});
  
  if(urlParts.pathname == "/insert") {
    /* Insert into table */
    meetingTable[query.id] = query.ip;
    console.log("Meeting table: ", meetingTable);

    /* Update the presistent file for use during recovery */
    fs.writeFile("files/meetings", JSON.stringify(meetingTable), function(err) {
      if(err) {
        console.log(err);
      }
    });

    response.end("Inserted!\n");
  }
  else if(urlParts.pathname == "/lookup") {
    /* Lookup in the table */
    if(meetingTable[query.id] == null) {
        response.end("0.0.0.0");
    }
    else {
        response.end(meetingTable[query.id]);
    }
  }
  else if(urlParts.pathname == "/table") {
    /* Print the table */
    response.end(JSON.stringify(meetingTable));
  }
  else if(urlParts.pathname == "/clear") {
    /* Clears the table */
    meetingTable = {};
    console.log("Meeting table: ", meetingTable);

    /* Update the presistent file for use during recovery */
    fs.writeFile("files/meetings", JSON.stringify(meetingTable), function(err) {
      if(err) {
        console.log(err);
      }
    });

    response.end("Table cleared!\n");
  }
  else {
    /* Invalid URL */
    response.end('Error!\n');
  }
}).listen(1337);
sys.log('Server running at port 1337..\n');
