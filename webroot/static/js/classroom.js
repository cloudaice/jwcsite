$(document).ready(function(){
    function check_checkbox(){
        var sections = new Array() ;
        $('#sections button').each(function(){
            var section = $(this).text();
            //console.debug(section);
            var classname = $(this).attr('class').split(' ');
            //console.debug(classname);
            //console.debug(classname[classname.length - 1]);
            if (classname[classname.length - 1] == 'active'){
                sections.push(section);
            }
        });
        return sections;
        //console.debug(sections.length);
    }
    
    //在循环中return并不会终止函数,只是终止循环
    function check_building(){
        var builds = new Array();
        $('#buildTab li').each(function(){
            if ($(this).hasClass('active')){
                var buildname = $(this).children('a').text();
                builds.push(buildname);
            }
        });
        return builds;
    }

    //点击building 的时候,检查选择的节次并且显示.
    $('#buildTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
        var buildname = $(this).text();
        console.debug(buildname);
        var sections = check_checkbox();
        for (var i in sections){
            console.debug(sections[i]);
        }

    });

    //点击button的时候，检查building是否已经选择, 有则显示，否则不显示
    $('#sections button').click(function(){
        $(this).button('toggle');
        var builds = check_building();
        if(builds.length != 0){
            console.debug(builds[0]);
            var sections = check_checkbox();
            for (var i in sections){
                console.debug(sections[i]);
            }
        }
    });
});
