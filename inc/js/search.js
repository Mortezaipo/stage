$(document).ready(function(){
    if (!window.location.hash)
        $("#search-keyword").focus();

    $("#search-keyword").keyup(function(){
        search_keyword = $("#search-keyword").val().toLowerCase();
        if (!search_keyword.match("^[a-zA-Z0-9\_\-]+$"))
            return false;

        $(".tag-item").each(function(index, element){
            title = $(element).find(".tag-title").text()
            if (title.toLowerCase().search(search_keyword) == -1) {
                $(element).hide();
            } else {
                $(element).show();
            }

            $(element).find(".post-title").each(function(s_index, s_element){
                s_title = $(s_element).text();
                if (s_title.toLowerCase().search(search_keyword) == -1) {
                    $(s_element).removeClass("search-highlight");
                } else {
                    $(s_element).addClass("search-highlight").show();
                    $(element).show();
                }
            });
        });

        if (search_keyword == ""){
            $(".tag-item").each(function(index, element){
                $(element).show();
                $(element).find(".post-title").each(function(s_index, s_element){
                    $(s_element).children("strong").removeClass("search-highlight");
                });
            });
        }
    });
    $("#search-keyword").on('input', function(){
        search_keyword = $("#search-keyword").val().toLowerCase()
        if (search_keyword == "") {
            $(".tag-item").each(function(index, element){
                $(element).show();
                $(element).find(".post-title").each(function(s_index, s_element){
                    $(s_element).children("strong").removeClass("search-highlight");
                });
            });
        }
    });
});
