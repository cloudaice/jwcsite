$(document).ready(function(){
    $("#query-curriculum").autocomplete({
        minlength: 2,
        max: 5,
        autoFocus: true,
        delay: 50,
        source: function(request, response){
            var url = '/Teac_Course';
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
        }
    });
    function load_course_table(){
        var url = "/curriculum"
        var param = {
            'query_string': $("input[id='query-curriculum']").val()
        }
        $.ajax({
            type: 'POST',
            url: url,
            data: param,
            dataType: 'json',
            success: function(data){
                var course_table = "<table class='table table-striped'>";
                course_table += "<thead><tr>";
                course_table += "<th>课程</th>";
                course_table += "<th>教师</th>";
                course_table += "<th>上课地点</th>";
                course_table += "<th>星期</th>";
                course_table += "<th>节次</th>";
                course_table += "<th>起止周</th>";
                course_table += "</tr></thead>";
                course_table += "<tbody>";
                console.debug(data);
                for (var i in data){
                    course_table += "<tr>";
                    course_table += "<td class='solid'>" + data[i]['course'] + "</td>";
                    course_table += "<td class='solid'>" + data[i]['teacher'] + "</td>";
                    course_table += "<td class='solid'>" + data[i]['addr'] + "</td>";
                    course_table += "<td class='solid'>" + data[i]['weekday'] + "</td>";
                    course_table += "<td class='solid'>" + data[i]['section'] + "</td>";
                    course_table += "<td class='solid'>" + data[i]['startend'] + "</td>";
                    course_table +="</tr>";
                }
                course_table += "</tbody></table>";
                $('#course_table').html(course_table);
            }
        });
    }
    $("#query-curriculum").bind('keyup', function(event){
        if (event.keyCode == "13"){
            load_course_table();
        }
    });

    $('#search-button').click(function(){
        load_course_table();
    });

});
