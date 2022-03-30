var connection = require('./connection');
var request = require('superagent');
var python_url = 'http://127.0.0.1:5000'

function User() {

  this.get = function(res) {
    console.log("Get all user");
    connection.acquire(function(err, con) {
      con.query('select * from users', function(err, result) {
        con.release();
        res.send(result);
      });
    });
  };

  this.callPython = function(res) {
	request.get(python_url + '/test_connect')
	  .end(function(err, resp) {
	    res.send(resp);
	  });
  }
}
module.exports = new User();


