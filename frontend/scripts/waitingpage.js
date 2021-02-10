app.controller('clientWaitingController', function($scope, api, $window) {

  timer = setInterval(function(){ $scope.login_status() }, 30000);
  $scope.model_data = JSON.parse(sessionStorage.getItem('clientinfo'));//{'name': '', 'email': '', 'company': ''}
  if($scope.model_data == undefined){
    $window.location.href = '/#!/'
  }
  $scope.login_status = function (){
    console.log($scope.model_data);
    api.call("POST", "requeststatus/", $scope.model_data).then(function(response){
      console.log(response);
      if(response.status == 200){
        clearInterval(timer);
        $window.location.href = '/#!/loginaccept';
      }
      else if(response.status == 401){
        clearInterval(timer);
        alert("Admin Rejected the Login Request")
        sessionStorage.clear();
        $window.location.href = '/#!/'
      }
    });
  }


});
