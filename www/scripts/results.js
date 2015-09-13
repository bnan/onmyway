function drawMap(idx, interests, limit) {
    $('#results .mdl-spinner').show();
    $('#map').hide();

    var load_currentLocation = load('currentLocation');
    var load_routes = load('routes');

    if (!load_currentLocation || !load_routes) {
        GMaps.geolocate({
            success: function (location) {
                var currentLocation = {'lat': location.coords.latitude, 'lng': location.coords.longitude};

                $.get('http://178.62.17.170:1337/circuits/' + currentLocation['lat'] + ',' + currentLocation['lng'] + '/' + interests + '/' + limit + '/', function (all_routes) {
                    console.log(all_routes);
                    save(currentLocation, all_routes);
                    $('#results .mdl-spinner').hide();
                    $('#map').show();
                    var map = new GMaps({
                        div: '#map',
                        lat: currentLocation['lat'],
                        lng: currentLocation['lng'],
                        disableDefaultUI: true
                    });
                    drawPath(map, currentLocation, all_routes[idx]);
                });

            },
            error: function (error) {
                alert('Geolocation failed: ' + error.message);
            }

            ,
            not_supported: function () {
                alert('Your browser does not support geolocation');
            }
            ,
            always: function () {
            }
        });
    }
    else {
        var currentLocation = load_currentLocation;
        var all_routes = load_routes;

        $('#results .mdl-spinner').hide();
        $('#map').show();

        var map = new GMaps({
            el: '#map',
            lat: currentLocation['lat'],
            lng: currentLocation['lng'],
            disableDefaultUI: true
        });
        drawPath(map, currentLocation, all_routes[idx]);
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
