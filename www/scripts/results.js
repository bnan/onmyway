var map;
var currentPosition;

GMaps.geolocate({
    success: function(position) {
        latitude = position.coords.latitude;
        longitude = position.coords.longitude;

        currentPosition = {
            'location': {
                'lat': latitude,
                'lng': longitude
            }
        };

        console.log(currentPosition);

        map = new GMaps({
            el: '#map',
            'lat': latitude,
            'lng': longitude
        });
    },
    error: function(error) {
        alert('Geolocation failed: '+error.message);
    },
    not_supported: function() {
        alert("Your browser does not support geolocation");
    },
    always: function() {
        alert("Done!");
    }
});

$.get("http://127.0.0.1:1337/circuits/43.343434,43.43434343/5/coffee", function(places) {
    places.forEach(function(place) {
        map.addMarker({
            lat: place.location.lat,
            lng: place.location.lng,
            title: place.name,
            click: function(e) {
                alert('You clicked in this marker');
            }
        });
    });

});
