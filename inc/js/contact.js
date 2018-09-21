$(document).ready(function(){
    $("#submit-message").click(function(e){
        $(this).attr("disabled", "disabled");
        $("#submit-result").hide();
        $("#form-process").fadeIn('fast');
        $.post($("#contact-form").attr("action"), $("#contact-form").serialize(), function(result) {
            console.log(result);
            if(result["result"] == "error") {
                $("#submit-result").html('<div class="alert alert-danger"><i class="fa fa-exclamation-triangle"></i> Sending message failed. Please check your inputs.</div>');
            }
            else {
                $("#submit-result").html('<div class="alert alert-success"><i class="fa fa-check-circle"></i> Message sent successfully.</div>');
                $("#contact-form").trigger("reset");
            }
            $("#submit-result").show();
            $("#submit-message").removeAttr("disabled");
            $("#form-process").fadeOut('fast');
        });
    });
});