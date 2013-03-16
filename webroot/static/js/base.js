$(document).ready(function(){
    url = window.location.href;
    //$('#topTab').children().removeClass('active');
    lasturl = url.split('/');
    classname = '/' + lasturl[lasturl.length-1];
    //console.debug(classname);
    //console.debug($("[href='" + classname + "']").text());
    //$("[href='" + classname + "']").addClass('active');
});
