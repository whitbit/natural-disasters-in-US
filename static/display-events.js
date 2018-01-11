$('#filter').on('submit', filterEvents);

function filterEvents(evt) {

    evt.preventDefault();

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