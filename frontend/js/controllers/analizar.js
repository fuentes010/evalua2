(function(){
    'use strict';

    angular
    .module('evalua2')
    .controller('analizarController', ['$scope', '$stateParams', 'AnalizarFactory', function($scope, $stateParams, AnalizarFactory){

        $scope.analysis = [];
        $scope.uploaded_json = [];

        $scope.uploadFile = function() {
            $('#upload-file').click();
        };

        $scope.fileUploaded = function(element){
            var file = element.files[0];
            var reader = new FileReader();
            reader.onload = function() {
                $scope.uploaded_json = JSON.parse(this.result);
                $scope.analysis = AnalizarFactory.save($scope.uploaded_json);
                $scope.$apply();
            }
           reader.readAsText(file);
        };

    }]);

})();