function menuclick(id) {
    var checked = document.querySelector('#' + id).checked;
    $('#' + id).prop('checked', !checked);
}

var cenas = true;

$(document).ready(function() {
    $(".trigger").on('click', function() {
        if(cenas)
            {
            $(".menu").addClass("active");
            console.log('banana');
            cenas = false;
        }
        else
        {
            console.log('pila');
        }

    });

});
