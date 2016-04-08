
$("#ChantierIndexForm").submit(function (e) {

    e.preventDefault() ;

    var data = $(this).serialize();

    $("#loader").attr("style", "display:block");

    $.ajax({
        url: "/Shops/search",
        type: "POST",
        data: data,
        dataType: "html",


        success : function(code_html, statut){
            $("#result").html(code_html);
        },

        error : function(resultat, statut, erreur){
            alert("Une erreur est survenue lors de l'appel au serveur");
        },

        complete : function(resultat, statut){
            $("#loader").attr("style", "display:none")
        }

    });
});


$("#ChantierIndexForm").ready(function () {
    $("#ChantierIndexForm").trigger("submit");
});


$('#load_more').click(function (event) {
    event.preventDefault();//to don't go to the top of the page
    //I take the input value and I add one
    var n_page = $('#n_page');
    var val_n_page = n_page.val()
    n_page.val(++val_n_page);
    //and I submit the form
    $('#ChantierIndexForm').trigger('submit');
});

$('#submit').click(function () {
    $('#n_page').val(1);
});


$('#recherche_but').click(function () {
    $("#ChantierIndexForm").toggle('clip');
    console.debug('recherche_but clicked');
});