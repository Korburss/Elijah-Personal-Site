/* Store UTM parameters for the life of a browser tab. These can be used in form submissions or dynamic content */

if (location.search.length > 0) {
    const utm = new URLSearchParams(location.search);
    sessionStorage.setItem("Form_URL", location.host + location.pathname);
    utm.forEach(function utmSetter(value, key) {
        sessionStorage.setItem(key, value);
    });
}

