function drawMap(idx, interests, limit) {
    $('#results .mdl-spinner').show();
    $('#map').hide();

    var loadCurrentLocation = load('currentLocation');
    var loadRoutes = load('routes');

    if (!loadCurrentLocation || !loadRoutes) {
        GMaps.geolocate({
            success: function (location) {
                var currentLocation = {
                    'lat': location.coords.latitude,
                    'lng': location.coords.longitude
                };

                var url = 'http://178.62.17.170:1337/circuits/' + currentLocation['lat'] + ',' + currentLocation['lng'] + '/' + interests + '/' + limit + '/';

                $.get(url, function (allRoutes) {
                    console.log(allRoutes);
                    save(currentLocation, allRoutes);

                    $('#results .mdl-spinner').hide();
                    $('#map').show();

                    var map = new GMaps({
                        div: '#map',
                        lat: currentLocation['lat'],
                        lng: currentLocation['lng'],
                        disableDefaultUI: true
                    });

                    drawPath(map, currentLocation, allRoutes[idx]);
                });

            },
            error: function (error) {
                alert('Geolocation failed: ' + error.message);
            },
            not_supported: function () {
                alert('Your browser does not support geolocation');
            },
            always: function () {
            }
        });
    }
    else {
        var currentLocation = loadCurrentLocation;
        var allRoutes = loadRoutes;

        $('#results .mdl-spinner').hide();
        $('#map').show();

        var map = new GMaps({
            el: '#map',
            lat: currentLocation['lat'],
            lng: currentLocation['lng'],
            disableDefaultUI: true
        });

        drawPath(map, currentLocation, allRoutes[idx]);
    }
}

function drawPath(map, currentLocation, route) {
    map.addMarker({
        lat: currentLocation['lat'],
        lng: currentLocation['lng'],
        title: 'Current Location',
        infoWindow: {
            content: '<p>You are here!</p>'
        }
    });

    route.forEach(function (place) {
        map.addMarker({
            lat: place.location.lat,
            lng: place.location.lng,
            title: place.name,
            icon: place.icon,
            infoWindow: {
                content: place.name
            }
        });
    });

    if (route.length) {
        map.drawRoute({
            origin: [currentLocation['lat'], currentLocation['lng']],
            destination: [route[0]['location']['lat'], route[0]['location']['lng']],
            travelMode: 'walking',
            strokeColor: '#ff0000',
            strokeOpacity: 0.6,
            strokeWeight: 6
        });
    }

    for (var i = 1; i < route.length; i++) {
        var origin = [route[i - 1]['location']['lat'], route[i - 1]['location']['lng']];
        var destination = [route[i]['location']['lat'], route[i]['location']['lng']];

        map.drawRoute({
            origin: origin,
            destination: destination,
            travelMode: 'walking',
            strokeColor: '#ff0000',
            strokeOpacity: 0.6,
            strokeWeight: 6
        });
    }
}
