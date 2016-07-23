(function(){
    'use strict';

    angular
    .module('evalua2')
    .controller('mainController', ['$scope', function($scope){

        $scope.logged = true;
        $scope.doLogin = function(){
            //TODO: Implementar un login contra la RESTAPI
            $scope.logged = true;
        }

    }]);

})();