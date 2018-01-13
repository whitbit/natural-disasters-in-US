mapboxgl.accessToken = 'pk.eyJ1Ijoid2hpdGJpdCIsImEiOiJjamNjZGFrdWwxNTY3MnlyM2VlcG9obngzIn0.toHPmitLn7fQbQn5NZHJrQ';

  var map = new mapboxgl.Map({
    container: 'map',
    maxZoom: 5.5,
    minZoom: 1.8,
    style: 'mapbox://styles/mapbox/light-v9',
    center: [-115.36957574368233, 40.732480262447524],
    zoom: 2
  });

  map.on('load', function () {

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
              [0, '#70F1FF'],
              [10, '#56D7FF'],
              [20, '#3DBEFF'],
              [50, '#23A4FF'],
              [100, '#0A8BE6'],
              [200, '#0071CC'],
              [500, '#0058B3'],
              [1000, '#003E99']
          ]
        },
        'fill-opacity': 0.75
      }
    }, firstSymbolId);
  });

  map.on('click', 'us-states', function(e) {
    var coordinates = almostFlatten(e.features[0].geometry.coordinates);
    var bounds = new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]);
    coordinates.forEach(function(coord) {
      bounds.extend(coord);
    })

    map.fitBounds(bounds, { padding: 100 });
  });


  function almostFlatten(arr) {
    return arr.reduce(function (flat, toFlatten) {
      return flat.concat(Array.isArray(toFlatten[0]) ? almostFlatten(toFlatten) : [toFlatten]);
    }, []);
  }