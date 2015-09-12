function menuclick(id) {
    var checked = document.querySelector('#' + id).checked;

    if(!checked) {
        $('#' + id + '-btn i.fa').css({'color': 'yellow'});
    } else {
        $('#' + id + '-btn i.fa').css({'color': 'white'});
    }

    $('#' + id).prop('checked', !checked);
}

var isToggled = true;

$(document).ready(function() {
    $(".trigger").on('click', function() {
        if(isToggled) {
            $(".menu").addClass("active");
            isToggled = false;
        } else {
            var interests = $("[id^=interests]:checked").map(function() {
                return this.value;
            }).get();

            console.log(interests);

            var number_of_places = 5;

            // todo: toggle page
            drawMaps(interests, number_of_places);
        }

    });
});
