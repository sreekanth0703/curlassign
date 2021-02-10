app.controller('clientRequestController', function($scope, api, $window) {
  $scope.model_data = {'name': '', 'email': '', 'company': ''}
  $scope.login_request = function (){
    console.log($scope.model_data);
    api.call("POST", "loginrequest/", $scope.model_data).then(function(response){
      console.log(response);
      if(response.status == 201){
        $window.location.href = '/#!/clientwaiting';
        sessionStorage.setItem('clientinfo', JSON.stringify(response.data));
      }
    });
  }

});
