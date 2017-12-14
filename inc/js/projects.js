function load_projects() {
    $.get('https://api.github.com/users/mortezaipo/repos', function(data) {
    $('#projects_list #load').remove();
    jQuery.each(data, function(i, v){
        if(v.name != 'stage') //ignore my website project.
        {
            code_fork = '';
            if(v.fork == true) code_fork = ' <i class="fa fa-code-fork"></i>'
            $('#projects_list tbody')
                .append($("<tr>")
                    .append($('<td class="vertical-center text-center">').append(i+1))
                    .append($('<td class="vertical-center">').append(v.name.replace('-',' ').replace('_',' ') + code_fork))
                    .append($('<td class="vertical-center">').append(v.description))
                    .append($('<td class="vertical-center">').append(v.updated_at.substring(0, 10)))
                    .append($('<td>').append(
                        $('<a>').attr({href:v.html_url, class:'btn btn-sm btn-outline-info btn-block', target:'_blank'}).html('<i class="fa fa-github"></i> Source'))
                    )
                );
            }
        });
    });
}

$("document").ready(function() {
    load_projects();
});
