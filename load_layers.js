// A base layer from Open Street Maps to use in the magnifying glass itself
// There is no user-facing toggle for this layer (besides the magnifying glass itself)
var osmBase = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    maxZoom: 22,
    attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
});

// The map base layer, served from Mapbox (== "Modern street map" in the key)
// var base = L.tileLayer('https://api.mapbox.com/styles/v1/a9696/cj1vva584000i2rkx28aayjh3/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYTk2OTYiLCJhIjoiY2lvaG8zdHh3MDA3Y3VobTFxYTZ2YTZzYiJ9.BboErVkpHLXjCUIKqR3xHQ', {
// maxZoom: 20
// })

// Another base layer from Carto... maybe I like better....
var base = new L.TileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    maxZoom: 19,
    subdomains: 'abcd',
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});

// National Registry of Historic Places points layer (local, load from a geojson)
var historicPlaces = L.geoJson(al_historic, {
    pointToLayer: function(feature, latlng) {
        return L.marker(latlng, {
                opacity: 1.0,
                //title: feature.properties.name,
                riseOnHover: true
            })
            .bindTooltip(feature.properties.name)
            .bindPopup("<b>" + feature.properties.name + "</b><br />" + feature.properties.desc);
    }
});
// Make the Historic Places into a ClusterMarker layer
var historicClusterMarkers = L.markerClusterGroup({
    disableClusteringAtZoom: 16
});
historicClusterMarkers.addLayer(historicPlaces);


// Load the National Historic Places points again, to use the layer within the
// magnifying glass it has to be loaded twice. Prepended with "mag" to differentiate
// from the other, identical Historic Place layer.
var magHistoricPlaces = L.geoJson(al_historic, {
    pointToLayer: function(feature, latlng) {
        return L.marker(latlng, {
                opacity: 1.0,
                //title: feature.properties.name,
                riseOnHover: true
            })
            .bindTooltip(feature.properties.name)
            .bindPopup("<b>" + feature.properties.name + "</b><br />" + feature.properties.desc);
    }
});
// Make into ClusterMarkers
var magHistoricClusterMarkers = L.markerClusterGroup({
    disableClusteringAtZoom: 16
});
magHistoricClusterMarkers.addLayer(magHistoricPlaces);


// Historic map rasters from Mapbox (make sure to load as static rasters, NOT styles!)
var mobile1838 = L.tileLayer('https://api.mapbox.com/v4/a9696.3qd94pcr/{z}/{x}/{y}.png128?access_token=pk.eyJ1IjoiYTk2OTYiLCJhIjoiY2lvaG8zdHh3MDA3Y3VobTFxYTZ2YTZzYiJ9.BboErVkpHLXjCUIKqR3xHQ', {
    minZoom: 10,
    maxZoom: 21
});

var mobile1900 = L.tileLayer('https://api.mapbox.com/v4/a9696.0frs8amb/{z}/{x}/{y}.png128?access_token=pk.eyJ1IjoiYTk2OTYiLCJhIjoiY2lvaG8zdHh3MDA3Y3VobTFxYTZ2YTZzYiJ9.BboErVkpHLXjCUIKqR3xHQ', {
    minZoom: 10,
    maxZoom: 21
});