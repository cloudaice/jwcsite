$(document).ready(function(){
    function check_checkbox(){

    }
    $('#buildTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
        var buildname = $(this).text();
        console.debug($(this).text())

    });

    console.debug('hello');
});
