$(document).ready(function(){

    //$("#results-table").tablesorter();
    paginate_table();
    var ctx = document.getElementById("chart-area").getContext("2d");
    var ctx2 = document.getElementById("chart-area-2").getContext("2d");

    $.ajax({
            url: '/get_bloom_stats',
            contentType: "application/json; charset=utf-8",
            type: 'POST',
            data: "bloom",
            success: function(response) {
                console.log(response);
                new Chart(ctx).Doughnut(response['values'], {animateScale: true});
            },
            error: function(error) {
                console.log(error);
            }
    });

    $.ajax({
            url: '/get_bloom_stats',
            contentType: "application/json; charset=utf-8",
            type: 'POST',
            data: "bloom_revisado",
            success: function(response) {
                console.log(response);
                new Chart(ctx2).Doughnut(response['values'], {animateScale: true});
            },
            error: function(error) {
                console.log(error);
            }
    });



    //new Chart(ctx2).Doughnut(data, {animateScale: true});

});

function paginate_table(){
    var CURRENT_PAGE = 0
    var TR_MAX = 20;
    var _trs = $('.tr-row');
    var _pages = Math.round(_trs.length / TR_MAX);
    if(_pages > 1){

      var _table = $('#results-table');
      //Evento para paginar la tabla
      _table.bind('repaginate', function() {
          /* Escondemos todos los tr
           * Seleccionamos el intervalo de la pagina y el numero de elementos por pagina
           * utilizando la funcion slice y los mostramos.
           */
          _table.find('tbody tr').hide().slice(CURRENT_PAGE * TR_MAX, (CURRENT_PAGE + 1) * TR_MAX).show();
      });
      _table.trigger('repaginate');


      $('.pagination').twbsPagination({
          totalPages: _pages,
          visiblePages: 8,
          first: '<<',
          prev: '<',
          next:'>',
          last:'>>',
          onPageClick: function (event, page) {
            CURRENT_PAGE = page-1;
            _table.trigger('repaginate');
            $(this).addClass('active').siblings().removeClass('active');
          }
      });

    }



}
