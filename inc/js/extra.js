$(document).ready(function(){
    $.get("https://api.github.com/users/mortezaipo/repos", function(data) {
        $("#projects_list #load").remove();
        jQuery.each(data, function(i, v){
            $("#projects_list tbody")
                .append($("<tr>")
                    .append($("<td>").append(i+1))
                    .append($("<td>").append(v.name))
                    .append($("<td>").append(v.description))
                    .append($("<td>").append(v.updated_at))
                    .append($("<td>").append(
                        $("<a>").attr({href: v.html_url, class: 'btn btn-xs btn-default'}).html("Source"))
                    )
                );
        });
    });
});