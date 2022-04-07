angular.module('myApp')
  .controller('manageUserCtrl', function($scope, $http) { 'use strict';
    $scope.title = "Trang Manage User"

    $scope.refreshUsers = function() {
      var current = this;
      $http.get('/user').then(function(result) {
         $scope.listUsers = current.calAge(result.data);
      });
    }

    $scope.connectPython = function() {
    	$http.get('/connect_python').then(function(result) {
    	var data = JSON.parse(result.data.text);
        alert(data.data); 
      });
    }
})

