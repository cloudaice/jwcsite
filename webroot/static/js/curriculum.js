$(document).ready(function(){
    $("#query-curriculum").autocomplete({
        source: function(request, response){
            url = '/Teac_Course';
            $.ajax({
                type: 'POST',
                url: url,
                data: {
                    'query_string': request.term
                },
                dataType: 'json',
                success: function(data){
                    console.debug(data);
                    response($.map(data, function(item){
                        console.debug(item);
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minlength: 2,
        autoFocus: true,
        delay: 500
    });
});
