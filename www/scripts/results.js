function drawMaps(interests, limit) {
    var load_currentLocation = load('currentLocation');
    var load_routes = load('routes');
    if (!load_currentLocation || !load_routes) {
        GMaps.geolocate({
            success: function (location) {
                var currentLocation = {'lat': location.coords.latitude, 'lng': location.coords.longitude};

                var map0 = new GMaps({
                    div: '#map0',
                    lat: currentLocation['lat'],
                    lng: currentLocation['lng'],
                    disableDefaultUI: true
                });

                var map1 = new GMaps({
                    div: '#map1',
                    lat: currentLocation['lat'],
                    lng: currentLocation['lng'],
                    disableDefaultUI: true
                });

                var map2 = new GMaps({
                    div: '#map2',
                    lat: currentLocation['lat'],
                    lng: currentLocation['lng'],
                    disableDefaultUI: true
                });

                $.get('http://178.62.17.170:1337/circuits/' + currentLocation['lat'] + ',' + currentLocation['lng'] + '/' + interests + '/' + limit + '/', function (all_routes) {
                    console.log(all_routes);
                    save(currentLocation, all_routes);
                    drawRoute(map0, currentLocation, all_routes[0]);
                    drawRoute(map1, currentLocation, all_routes[1]);
                    drawRoute(map2, currentLocation, all_routes[2]);
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
                $('.page-content--results .mdl-spinner').hide();
            }
        });
    }
    else {
        var currentLocation = load_currentLocation;
        var all_routes = load_routes;

        var map0 = new GMaps({
            div: '#map0',
            lat: currentLocation['lat'],
            lng: currentLocation['lng'],
            disableDefaultUI: true
        });

        var map1 = new GMaps({
            div: '#map1',
            lat: currentLocation['lat'],
            lng: currentLocation['lng'],
            disableDefaultUI: true
        });

        var map2 = new GMaps({
            div: '#map2',
            lat: currentLocation['lat'],
            lng: currentLocation['lng'],
            disableDefaultUI: true
        });

        drawRoute(map0, currentLocation, all_routes[0]);
        drawRoute(map1, currentLocation, all_routes[1]);
        drawRoute(map2, currentLocation, all_routes[2]);
    }
}

function drawRoute(map, currentLocation, route) {
    map.addMarker({
        lat: currentLocation['lat'],
        lng: currentLocation['lng'],
        title: 'Current Location',
        infoWindow: {
            content: '<p>Big Ben is the nickname for the great bell of the clock at the north end of the Palace of Westminster in London, and often extended to refer to the clock and the clock tower, officially named Elizabeth Tower.</p>'
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
            origin: currentLocation,
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
