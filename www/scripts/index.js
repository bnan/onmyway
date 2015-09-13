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

    if(index.is(':visible')) {
        $('#load-message').hide();
    }
}

var isToggled = true;

$(document).ready(function() {
    if (load('currentLocation') && load('routes')) {
        switchPageView();
        drawMap(0, interests, 5);

        $('#load-message').show();

        $('#load-message-btn').on('click', function() {
            $('#load-message').hide();
        });
    }
    // else {
    //     // $('#load-message').hide();
    // }

    $(".trigger").on('click', function() {
        if(isToggled) {
            $(".menu").addClass("active");
            $(".trigger i.fa").removeClass("fa-bars");
            $(".trigger i.fa").addClass("fa-search");
            isToggled = false;
        } else {
            interests = $("[id^=interests]:checked").map(function() {
                return this.value;
            }).get();

            console.log(interests);
            interests = interests.toString();

            switchPageView();
            drawMap(0, interests, 5);
        };
    });



    $('#results-icon').on('click', function() {
        remove(['currentLocation', 'routes']);
        switchPageView();
    });

    $('#tab0').on('click', function() {
        drawMap(0, interests, 5);
    });

    $('#tab1').on('click', function() {
        drawMap(1, interests, 5);
    });

    $('#tab2').on('click', function() {
        drawMap(2, interests, 5);
    });


});
