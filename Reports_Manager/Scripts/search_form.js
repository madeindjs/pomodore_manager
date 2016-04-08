
$("#ChantierIndexForm").submit(function (e) {

    e.preventDefault() ;

    var data = $(this).serialize();

    $.ajax({
        url: "/Shops/search",
        type: "POST",
        data: data,
        dataType: "html",
        success : function(code_html, statut){
            $("#result").html(code_html);
        },

        error : function(resultat, statut, erreur){
         
        },

        complete : function(resultat, statut){

        }

    });
});


$("#ChantierIndexForm").ready(function () {
    $("#ChantierIndexForm").trigger("submit");
});

$("#test").click(function () {
    $("#ChantierIndexForm").trigger("submit");
});