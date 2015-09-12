function save(currentLocation, places) {
    localStorage.setItem('currentLocation', JSON.stringify(currentLocation));
    localStorage.setItem('places', JSON.stringify(places));
}

function load() {
    return JSON.parse(localStorage.getItem('places'));
}