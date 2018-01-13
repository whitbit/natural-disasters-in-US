$('#filter').on('submit', filterEvents);

function filterEvents(evt) {

    evt.preventDefault();

    $.ajax({
        url: '/api/events',
        data: $('form').serialize(),
        type: 'GET',
        success: function(results) {
            rendersFilteredEvents(results),
            rendersMapDensities(results)
        },
        error: function(error) {
            console.log(error)
        }
    })
}

function rendersFilteredEvents(results) {
    
    $('td').empty();

    for(var i = 0; i < results.length; i++) {
        $('table').append(buildTableRow(results[i]));
    }
}


function buildTableRow(event) {
    var state = event['state']
    var incidentType = event['incidentType']
    var startDate = event['startDate']
    var count = event['count']
    
    return '<tr>\
                <td>' + state + '</td> \
                <td>' + incidentType + '</td> \
                <td>' + startDate + '</td>\
                <td>' + count + '</td>\
            <tr>'
}

function rendersMapDensities(results) {
    
}