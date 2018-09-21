function load_projects() {
    $.get('https://api.github.com/users/mortezaipo/repos', function(data) {
    $('#projects-list #load').remove();
    jQuery.each(data, function(i, v){
        if(v.name != 'stage') //ignore my website project.
        {
            tag_data = $.get("https://api.github.com/repos/mortezaipo/" + v.name + "/tags", function(tag_data) {
                if(tag_data.length)
                    state = "Released";
                else
                    state = "Dev";

                code_fork = '';
                if(v.fork == true) code_fork = ' <i class="fa fa-code-fork"></i>'
                $('#projects-list tbody')
                    .append($("<tr>")
                        .append($('<td class="text-center">').append(i+1))
                        .append($('<td>').append(v.name.replace('-',' ').replace('_',' ') + code_fork))
                        .append($('<td>').append(v.description))
                        .append($('<td>').append('<label class="badge badge-light">' + v.updated_at.substring(0, 10) + '</label>'))
                        .append($('<td>').append('<label class="badge badge-light">' + state + '</label>'))
                        .append($('<td class="text-center">').append(
                            $('<a>').attr({href:v.html_url, class:'src-links', target:'_blank'}).html('<i class="fab fa-github"></i>'))
                        )
                    );
                });
            }
        });
    });
}

$("document").ready(function() {
    load_projects();
});
