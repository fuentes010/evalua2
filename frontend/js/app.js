(function(){
    'use strict';

    angular.module('evalua2', ['ngMaterial', 'ui.router', 'ngResource', 'ngCookies', 'chart.js', 'ncy-angular-breadcrumb'])
           .config(function($mdThemingProvider, $stateProvider, $urlRouterProvider, $breadcrumbProvider, $httpProvider, $resourceProvider) {
                $resourceProvider.defaults.stripTrailingSlashes = false;

                $mdThemingProvider.theme('default')
                                  .primaryPalette('blue-grey')
                                  .accentPalette('orange');

                $breadcrumbProvider.setOptions({
                    template: '<div class="breadcrumb"><span ng-repeat="step in steps"> <a class="breadcrumb-step" href="{{step.ncyBreadcrumbLink}}">{{step.ncyBreadcrumbLabel}}</a> <span class="divider" ng-hide="$last">></span></span></div>'
                });

                $urlRouterProvider.otherwise('/');
                $stateProvider
                    .state('home', {
                                url: '/',
                                templateUrl : '/views/home.html',
                                controller  : "homeController",
                                ncyBreadcrumb: {
                                    label: 'Inicio'
                                }
                    })
                    .state('resultados-apredizaje', {
                                url: '/resultados-aprendizaje',
                                templateUrl : '/views/resultados_aprendizaje.html',
                                controller  : "resultadosApredizajeController",
                                ncyBreadcrumb: {
                                    label: 'Resultados aprendizaje',
                                    parent: 'home'
                                }
                    })
                    .state('resultados-apredizaje.asignatura', {
                                url: '/:asigId',
                                templateUrl: 'views/asignatura.html',
                                controller: 'asignaturaController',
                                ncyBreadcrumb: {
                                    label: '{{asignatura.name}}',
                                    parent: 'resultados-apredizaje'
                                }
                    })
                    .state('categorias-bloom', {
                                url: '/categorias-bloom',
                                templateUrl : '/views/categorias_bloom.html',
                                controller  : "categoriasBloomController",
                                ncyBreadcrumb: {
                                    label: 'Categorias bloom',
                                    parent: 'home'
                                }
                    })
                    .state('analizar', {
                                url: '/analizar',
                                templateUrl : '/views/analizar.html',
                                controller  : "analizarController",
                                ncyBreadcrumb: {
                                    label: 'Analizar',
                                    parent: 'home'
                                }
                    });
           })
           .run(function ($http, $cookies) {
                $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
           });

})();
