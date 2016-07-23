(function(){
    'use strict';

    angular
    .module('evalua2')
    .controller('asignaturaController', ['$scope', '$stateParams', 'AsignaturaFactory', function($scope, $stateParams, AsignaturaFactory){

        $scope.asignatura = {'name': 'NaN', 'values': []};
        $scope.asignatura_id = null;

        if($stateParams.asigId) {
            $scope.asignatura = AsignaturaFactory.get({'id':$stateParams.asigId});
            console.log($scope.asignatura);
        }

    }]);

})();

