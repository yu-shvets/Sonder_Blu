$('.like').on('click', function(event) {
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url: 'like',
        data: {movie_id: element.attr('data-id')},

        success: function(response){
            element.html('Likes: ' + response);
        }
    });
});

