$('#table_meubles input').change(function () {

    var delimiter = "_" ;

    if ($(this).is(':checked')) {

        //we change the current color
        $(this).parent().parent().css('font-weight', 'bold');

        //we get the serial number in table and then we concatenate in the form
        var n_serie = get_serie(this);



        
        $('#RapportSeries').val(function () {
            return $(this).val() + n_serie + delimiter;
        });
        

    } else {
        //we change the current color
        $(this).parent().parent().css('font-weight', 'normal');

        //we find the serial number in table and then we remove it in the form
        var series = $('#RapportSeries').val();
        $('#RapportSeries').val(series.replace(get_serie(this) + delimiter, ''));
    }


    function get_serie(objet) {
        return $(objet).parent().next().next().html();
    }

})