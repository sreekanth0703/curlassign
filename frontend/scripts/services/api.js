app.service('api', function($http, $q) {
  this.call = function (method, url, data) {
  var host = 'http://localhost:9003/api/';
  var d = $q.defer();
  $http({
    method : method,
      url : host + url,
      processData : false,
      contentType : false,
      data: data,
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      xhrFields: {
        withCredentials: true
      }
  }).then(function mySuccess(response) {
    d.resolve(response);
  }, function myError(response) {
    d.resolve(response);
  });
  return d.promise;
  }
});
