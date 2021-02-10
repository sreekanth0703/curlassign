var app = angular.module("myApp", ["ngRoute"]);
app.config(function($routeProvider) {
  $routeProvider
  .when("/", {
    templateUrl : "views/mainpage.html",
    //controller: "mainController"
  })
  .when("/login", {
    templateUrl : "views/login.html",
    controller: "loginController"
  })
  .when("/clientrequest", {
    templateUrl : "views/client_request.html",
  })
  .when("/clientwaiting", {
    templateUrl : "views/waitingpage.html"
  })
  .when("/loginaccept", {
    templateUrl : "views/login_accept.html",
  });
});

app.controller('mainController', function($scope, $http, api, $window) {
  $scope.check_status = function(){
    api.call("GET", "status/").then(function(response){
      console.log(response);
      if(response.status != 200){
        $window.location.href = '/#!/login/';
      }
    });
  }

  $scope.check_status();

  $scope.user_logout = function (){
    console.log($scope.model_data);
    api.call("GET", "user_logout/").then(function(response){
      console.log(response);
      if(response.status == 200){
        $window.location.href = '/#!/login/';
      }
    });
  }

  $scope.table_data = {};
  $scope.get_pending_requests = function(){
    api.call("GET", "loginrequest/").then(function(response){
      console.log(response);
      if(response.status == 200){
        $scope.table_data = response.data;
      }
    });
  }

  $scope.get_pending_requests();

 $scope.submit = function(dat, action){
    var sub_data = {"id": dat.id, "email": dat.email, "name": dat.name, "company": dat.company, "status": action}
    api.call("PUT", "loginrequest/", sub_data).then(function(response){
      console.log(response);
      if(response.status == 200){
        $scope.get_pending_requests();
      }
    });
 }

});
