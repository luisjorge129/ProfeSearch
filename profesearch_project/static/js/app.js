var search = angular.module('search', ['ngResource'])

search.run(function($http) {
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
});

search.config(function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

search.directive('a', function() {
    return {
        restrict: 'E',
        link: function(scope, elem, attrs) {
            if(attrs.ngClick || attrs.href === '' || attrs.href === '#'){
                elem.on('click', function(e){
                    e.preventDefault();
                });
            }
        }
   };
});

search.controller('SearchCtrl', function ($scope, $http, $sce) {
	$scope.submit = function(q) {
        if(typeof q !== "undefined"){
            $scope.searchData = "";
    		$scope.loading = true;
            url = 'search?q=' + q;
            $http.get(url)
            .success(function(out_data) {
            	$scope.searchData = $sce.trustAsHtml(out_data);
            	$scope.loading = false;
            });
            $scope.error_message = false;
        }else{
            $scope.error_message = "No se escribio ningun texto.";
        }
    }

    // $scope.pagination = function(url) {
    //     $scope.searchData = "";
    //     $scope.loading = true;
    //     url = 'search?url=' + url;
    //     $http.get(url)
    //     .success(function(out_data) {
    //         $scope.searchData = $sce.trustAsHtml(out_data);
    //         $scope.loading = false;
    //     });
    // }
})
