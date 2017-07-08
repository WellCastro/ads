$(document).ready(function() {
    $('#property').DataTable( {
        "language": {
            "lengthMenu": "Exibindo _MENU_ por página",
            "zeroRecords": "Nenhum registro",
            "info": "página _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro",
            "infoFiltered": "(filtered from _MAX_ total records)",
            'search': "Procurar:",
            paginate: {
                first:      "Primeira",
                previous:   "Anterior",
                next:       "Próxima",
                last:       "Última"
            }
        }
    } );
} );