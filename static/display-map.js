mapboxgl.accessToken = 'pk.eyJ1Ijoid2hpdGJpdCIsImEiOiJjamNjZGFrdWwxNTY3MnlyM2VlcG9obngzIn0.toHPmitLn7fQbQn5NZHJrQ';
    
var map = new mapboxgl.Map({
    container: 'map',
    maxZoom: 5.5,
    minZoom: 1.8,
    style: 'mapbox://styles/mapbox/light-v9',
    center: [-115.36957574368233, 40.732480262447524],
    zoom: 2.5
  });

map.on('load', renderMap);

function renderMap() {

  var layers = map.getStyle().layers;

  // Find the index of the first symbol layer in the map style
  var firstSymbolId;
  for (var i = 0; i < layers.length; i++) {
      if (layers[i].type === 'symbol') {
          firstSymbolId = layers[i].id;
          break;
      }
  }
  
  var statesLayer = map.addLayer({
    'id': 'us-states',
    'type': 'fill',
    'source': {
      type: 'geojson',
      data: statesData
    },
    'paint': {
      'fill-color': {
        property: 'density',
        stops: [
            [0, '#FFEDA0'],
            [10, '#FED976'],
            [20, '#FEB24C'],
            [50, '#FD8D3C'],
            [100, '#FC4E2A'],
            [200, '#E31A1C'],
            [500, '#BD0026'],
            [1000, '#500018']
        ]
      },
      'fill-opacity': 0.6
    }
  }, firstSymbolId);


}

map.on('mousemove', function(e) {
  var states = map.queryRenderedFeatures(e.point, {
    layers: ['us-states']
  });

  if (states.length > 0) {
    document.getElementById('pd').innerHTML = '<h3><strong>' + states[0].properties.name + '</strong></h3> \
                                              <p><strong><em>' + states[0].properties.density + '</strong> total occurence(s)</em></p>';
  } else {
    document.getElementById('pd').innerHTML = '<p>Hover over a state or scroll down for table details!</p>'
  }
});