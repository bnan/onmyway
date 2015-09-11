GMaps.geolocate({
    success: function (location) {
        var latitude = location.coords.latitude;
        var longitude = location.coords.longitude;

        var currentLocation = {
            'lat': latitude,
            'lng': longitude
        };

        console.log(currentLocation);

        var map = new GMaps({
            el: '#map',
            'lat': latitude,
            'lng': longitude
        });

        map.addMarker({
            lat: latitude,
            lng: longitude,
            title: 'Home.',
            click: function (e) {
                alert('You clicked in this marker');
            }
        });

        map.setCenter(latitude, longitude);

        $.get('http://192.168.43.215:1337/circuits/' + currentLocation['lat'] + ',' + currentLocation['lng'] + '/coffee/5/', function (places) {
            console.log(places);

            places.forEach(function (place) {
                map.addMarker({
                    lat: place.location.lat,
                    lng: place.location.lng,
                    title: place.name,
                    click: function (e) {
                        alert('You clicked in this marker');
                    }
                });
            });

            for (var i = 1; i < places.length; i++) {
                origin = [places[i - 1]['location']['lat'], places[i - 1]['location']['lng']];
                destination = [places[i]['location']['lat'], places[i]['location']['lng']];

                console.log(origin);
                console.log(destination);

                map.drawRoute({
                    origin: origin,
                    destination: destination,
                    travelMode: 'walking',
                    strokeColor: '#ff0000',
                    strokeOpacity: 0.6,
                    strokeWeight: 6
                });
            }
        });

    },
    error: function (error) {
        alert('Geolocation failed: ' + error.message);
    },
    not_supported: function () {
        alert('Your browser does not support geolocation');
    },
    always: function () {
        alert('Done!');
    }
});
