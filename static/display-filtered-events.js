$(document).ready(function() {
    $('#loading').fadeOut('slow');
})

$(window).on("load", displayFilterOptions);

function displayFilterOptions() {

    $.get('/event_types', function(results) {
        var filterOptions = document.getElementById('filter-options')
        var optionsStr = '';
        for(var i = 0; i < results.length; i++) {
            optionsStr += buildOptions(results[i][0]);
        }
        filterOptions.innerHTML = optionsStr
    }) 
}

function buildOptions(option) {

    return '<input type="checkbox" name="event_type" value="' + option 
           + '"<label for="' + option + '">' + option + '</label><br>'

}

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
    
    $('td').remove();

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

    var incidentDensities = getStateIncidentCounts(results);

    var updatedStatesData = updateStateDensityData(statesData, incidentDensities);
    
    map.getSource('us-states').setData(updatedStatesData);
}


function getStateIncidentCounts(results) {
    var stateDisasterCounts = {};

    for(var i = 0; i < results.length; i++) {
        var state = results[i]['state'];

        if (state in stateDisasterCounts) {
            stateDisasterCounts[state] = stateDisasterCounts[state] + results[i]['count']
        } else {
            stateDisasterCounts[state] = results[i]['count']
        }
    }

    return stateDisasterCounts
}


function convertToStateName(stateAbbrev) {
    var stateConversions = {
        'AL': 'Alabama',
        'AK': 'Alaska',
        'AZ': 'Arizona',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Deleware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NY': 'New York',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming'
    };

    return stateConversions[stateAbbrev]
}


function updateStateDensityData(statesData, incidentCounts) {

    var updatedStatesData = jQuery.extend(true, {}, statesData);

    for(state in incidentCounts) {
        
        for(var i = 0; i < updatedStatesData.features.length; i++) {
            if(convertToStateName(state) === updatedStatesData.features[i].properties.name) {
                updatedStatesData.features[i].properties.density = incidentCounts[state]
            }
        }
    }

    return updatedStatesData
}

