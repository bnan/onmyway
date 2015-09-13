var interests;

function menuclick(id) {
    var checked = document.querySelector('#' + id).checked;

    if(!checked) {
        $('#' + id + '-btn i.fa').css({'color': 'yellow'});
    } else {
        $('#' + id + '-btn i.fa').css({'color': 'white'});
    }

    $('#' + id).prop('checked', !checked);
}

function switchPageView() {
    var index = $('#index');
    index.toggle();
    var results = $('#results');
    results.toggle();
}

var isToggled = true;

$(document).ready(function() {
    $(".trigger").on('click', function() {
        if(isToggled) {

            $(".menu").addClass("active");
            isToggled = false;
        } else {
            interests = $("[id^=interests]:checked").map(function() {
                return this.value;
            }).get();

            console.log(interests);
            interests = interests.toString();

            switchPageView();
            drawMap('map0', interests, 5);
        }

    });

    $('#results-icon').on('click', function() {
        remove(['currentLocation', 'routes']);
        switchPageView();
    });
});
