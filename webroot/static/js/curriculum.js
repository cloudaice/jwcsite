$(document).ready(function(){
    $("#query-curriculum").autocomplete({
        source: function(request, response){
            url = '/Teac_Course';
            $.ajax({
                type: 'POST',
                url: url,
                data: param,
                dataType: 'json',
                success: function(data){
                }
                
            });
        },

    });
});
