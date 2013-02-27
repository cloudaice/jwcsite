$(document).ready(function(){
    $('#buildTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
    var s = $('.nav-tabs').button();
    console.debug('hello');
});
