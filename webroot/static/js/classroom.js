$(document).ready(function(){
    $('#buildTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
    console.debug('hello');
});
