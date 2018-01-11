$('#filter').on('submit', filterEvents);

function filterEvents(evt) {

    evt.preventDefault();

    // var formInputs = {
    //     'fromDate': $('#from').val(),
    //     'toDate': $('#to').val(),
    //     'event-type': "event-type"
    // };

    // $.get('/api/events', formInputs, rendersFilteredEvents);

    $.ajax({
        url: '/api/events',
        data: $('form').serialize(),
        type: 'GET',
        success: rendersFilteredEvents,
        error: function(error) {
            console.log(error)
        }
    })
}

function rendersFilteredEvents(results) {
    alert('It worked!')
}