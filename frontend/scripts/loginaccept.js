app.controller('loginAcceptController', function($scope, api, $window) {
  $scope.model_data = {}
  $scope.check_status = function(){
    api.call("GET", "status/").then(function(response){
      if(response.status == 200){
        $scope.model_data = response.data
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

});
