var user = require('../models/user');

module.exports = {
  configure: function(app) {
    app.get('/user', function(req, res) {
      user.get(res);
    });

    app.get('/connect_python', function(req, res) {
      user.callPython(res);
    });
  }
};