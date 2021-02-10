app.controller('loginController', function($scope, api, $window) {
  $scope.model_data = {'username': '', 'password': ''}
  $scope.login = function (){
    console.log($scope.model_data);
    api.call("POST", "user_login/", $scope.model_data).then(function(response){
      console.log(response);
      if(response.status == 200){
        $window.location.href = '/#!/';
      }
    });
  }

});
