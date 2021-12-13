jQuery("form").submit(function(){
    var submit_btn = jQuery('button[type="submit"]');
    submit_btn.attr('disabled', true);

    setTimeout(function(){
        submit_btn.removeAttr('disabled')
    }, 10000)

    return true
});