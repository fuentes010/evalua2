(function(){
    'use strict';

    angular
    .module('evalua2')
    .controller('categoriasBloomController', ['$scope', 'CategoriaBloomFactory', 'CategoriaBloomValorFactory', function($scope, CategoriaBloomFactory, CategoriaBloomValorFactory){

        $scope.labels = [];
        $scope.data = [[]];
        $scope.values = [];
        CategoriaBloomFactory.query(function(categorias){
            angular.forEach(categorias, function(categoria){
                $scope.labels.push(categoria.name);
                $scope.data[0].push(categoria.values.length);
                $scope.values.push(categoria.values);
            });
        });



    }]);

})();