$(document).ready(function(){
    function check_checkbox(){
        $('#sections button').each(function(){
            console.debug($(this).attr('class'));
            console.debug($(this).text());
        });
    }


    $('#buildTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
        var buildname = $(this).text();
        console.debug($(this).text())

    });

    $('#sections button').click(function(){
        $(this).button('toggle');
        check_checkbox();
    });

    console.debug('hello');
});
