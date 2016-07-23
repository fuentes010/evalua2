(function(){
    'use strict';

    angular
    .module('evalua2')
    .factory('CursoFactory', function($resource){
        return $resource('http://localhost:8000/api/v1/curso/:id');
    })
    .factory('AsignaturaFactory', function($resource){
        return $resource('http://localhost:8000/api/v1/asignatura/:id');
    })
    .factory('CategoriaBloomFactory', function($resource){
        return $resource('http://localhost:8000/api/v1/categoria-bloom/:id');
    })
    .factory('CategoriaBloomValorFactory', function($resource){
        return $resource('http://localhost:8000/api/v1/categoria-bloom-valor/:id');
    })
    .factory('AnalizarFactory', function ($resource) {
        return $resource('http://localhost:8000/api/v1/analizar/', {}, {
            save: {
                method: 'POST',
                isArray: true
            }
        });
    });

})();