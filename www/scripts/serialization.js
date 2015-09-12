function save(currentLocation, routes) {
    localStorage.setItem('currentLocation', JSON.stringify(currentLocation));
    localStorage.setItem('routes', JSON.stringify(routes));
}

function load(text) {  // Text should only be 'currentLocation' or 'places'
    return JSON.parse(localStorage.getItem(text));
}
