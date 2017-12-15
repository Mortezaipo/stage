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
                    $(s_element).removeClass("search-highlight");
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
                    $(s_element).removeClass("search-highlight");
                });
            });
        }
    });
    $("#search-btn").click(function(){
        keyword = $("#search_keyword").val()
        if(keyword.length > 2) {
            $("#search_keyword").removeClass("invalid-search-input");
            $("#search-modal").modal("toggle");
            google_search(keyword, $("#search-result"));
        } else {
            $("#search_keyword").addClass("invalid-search-input");
        }
    });
    $("#search-modal").on("hidden.bs.modal", function(e){
        $("#search-result").html('<div id="search-progress">Please wait... <i class="fa fa-spinner fa-pulse fa-fw"></i></div>');
    });
});

function google_search(keyword, element) {
    $.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyA_WzmLDuuI-4sxxfqdTdNf-gFGMqctP1g&cx=011378364823261141574:22pje6uhbnk&q=" + keyword, function(data) {
        if("items" in data) {
             for (i=0; i<data["items"].length; i++)
                 if (data["items"][i]["link"].search("\/posts\/page") > -1 || data["items"][i]["link"].search("\/tags\/") > -1)
                     continue
                 else {
                     $("#search-progress").remove();
                     title = data["items"][i]["title"].split(" - Morteza")[0]
                     link = data["items"][i]["link"];
                     $(element).append('<li><a href="' + link + '">' + title + '</a></li>');
                 }
        } else {
            $(element).append('<li><h1>Not Found :(</h1></li>');
        }
    });
}