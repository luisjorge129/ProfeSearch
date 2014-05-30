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

search.controller('SearchCtrl', function ($scope, $http, $sce) {
	$scope.submit = function(q) {
		$scope.searchData = ""
		$scope.loading = true;
        url = 'search?q=' + q
        $http.get(url)
        .success(function(out_data) {
        	$scope.searchData = $sce.trustAsHtml(out_data);
        	$scope.loading = false;
        });
    }

    $scope.pagination = function(page){
        $scope.searchData = ""
        $scope.loading = true;
        console.log(page);
        $http.get(page).success(function(out_data){
            $scope.searchData = $sce.trustAsHtml(out_data);
            $scope.loading = false;
        });
    }
})
