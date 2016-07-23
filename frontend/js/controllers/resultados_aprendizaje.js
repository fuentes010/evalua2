//http://www.upv.es/entidades/ETSINF/info/704863normalc.html

(function(){
    'use strict';

    angular
    .module('evalua2')
    .controller('resultadosApredizajeController', ['$scope', 'CursoFactory', function($scope, CursoFactory){

        $scope.cursos = [];
        $scope.asignaturas = [];
        CursoFactory.query(function(cursos){
            angular.forEach(cursos, function(curso){
                $scope.cursos.push(curso.name);
                $scope.asignaturas.push(curso.values);
            });
        });

    }]);

})();