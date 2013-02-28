$(document).ready(function(){
    var maps = {
        "第一节": 0,
        "第二节": 1,
        "第三节": 2,
        "第四节": 3,
        "第五节": 4,
    };
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
        //console.debug(buildname);
        var sections = check_checkbox();
        if (sections.length != 0){
            var num_sections = new Array();
            for (var i in sections){
                num_sections.push(maps[sections[i]]);
            }
            var url = '/classroom';
            var param = {
                "date": '2013-02-28',
                "build": buildname,
                "param": num_sections
            };
            console.debug(param);
            $.post(url, param, function(data){
                var room_table  = "<table class='table table-striped'>";
                data.each



            });
        }
    });

    //点击button的时候，检查building是否已经选择, 有则显示，否则不显示
    $('#sections button').click(function(){
        $(this).button('toggle');
        var builds = check_building();
        if(builds.length != 0){
            //console.debug(builds[0]);
            var sections = check_checkbox();
            var num_sections = new Array();
            for (var i in sections){
                num_sections.push(maps[sections[i]]);
            }
            var url = '/classroom'; 
            param = {
                "build": builds[0],
                "sections": num_sections
            }
            console.debug(param);
            //$.post(url, param, function(data){
                var room_table = "<table class='table table-striped'>"
                $('#room_table').html('hello');

            //});  
        }
    });
});
