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

$('.post_like').on('click', function(event) {
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url: 'post_like',
        data: {post_id: element.attr('data-id')},

        success: function(response){
            element.html('Likes: ' + response);
        }
    });
});

$('.comment_like').on('click', function(event) {
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url: 'comment_like',
        data: {node_id: element.attr('data-id')},

        success: function(response){
            element.html('Likes: ' + response);
        }
    });
});