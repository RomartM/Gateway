let media_fields = window.form_fields


/****
 * Dropzone Configuration
 * ****/

Dropzone.autoDiscover = false;
// Dropzone field conversion and initialization
media_fields.forEach((value, index)=>{
    // Cleanup and buildup
    let field = $("#id_"+value.id);
    media_fields[index].parent_instance = field.parent();
    media_fields[index].parent_instance.append(template(value.id, value.message))

    media_fields[index].form_params['csrfmiddlewaretoken'] = window.form_params.csrfmiddlewaretoken
    media_fields[index].form_params['field'] = "field_"+value.id
    media_fields[index].form_params['name'] = ''

    // Initialization
    media_fields[index].dropzone_instance = new Dropzone("#fileUpload_"+value.id, dropzone_config(value.id, media_fields[index].maxfiles, media_fields[index].form_params));

    field.remove()
})

jQuery(function($) {
    // Selectors
    let ajax_select_office = $('#ajax-select-unit');
    let ajax_select_purpose = $('#ajax-select-issue_type');

    const fuid_value = window.fuid()

    ajax_select_office
        .selectpicker({
            liveSearch: true
        })
        .ajaxSelectPicker({
            ajax: {
                method: 'GET',
                url: office_path,
                data: function() {
                    return {
                        q: '{{{q}}}'
                    };
                }
            },
            locale: {
                emptyTitle: 'Select..',
                statusInitialized: 'Start typing to select office'
            },
            preprocessData: function(data) {
                var array = []
                for (var i = 0; i < data.length; i++) {
                    var curr = data[i];
                    array.push({
                        'value': curr.id,
                        'text': curr.name
                    });
                }
                return array;
            },
            preserveSelected: true
        })
        .change(function() {
            var value = $(this).val();
            if (value) {
                $(this).removeAttr('required');
                $(this).parent().removeClass("is-invalid")
                ajax_select_purpose.removeAttr('disabled');
                ajax_select_purpose.siblings().removeClass('disabled');
            } else {
                $(this).attr('required', 'required');
                $(this).parent().addClass("is-invalid")
                ajax_select_purpose.attr('disabled');
                ajax_select_purpose.siblings().addClass('disabled');
            }
        });
        ajax_select_office.trigger('change').data('AjaxBootstrapSelect').list.cache = {}

    ajax_select_purpose
        .selectpicker({
            liveSearch: true
        })
        .ajaxSelectPicker({
            ajax: {
                method: 'GET',
                url: purposes_path,
                data: function() {
                    return {
                        o: ajax_select_office.val(),
                        q: '{{{q}}}'
                    };
                }
            },
            locale: {
                emptyTitle: 'Select..',
                statusInitialized: 'Start typing to select purpose'
            },
            preprocessData: function(data) {
                var array = [];
                if (Number(data.code) === 200) {
                    for (var i = 0; i < data.entries.length; i++) {
                        var curr = data.entries[i];
                        array.push({
                            'value': curr.id,
                            'text': curr.name
                        });
                    }
                } else {
                    var input_data = jQuery("#group-issue_type input").val()
                    array.push({
                        'value': 'tag_' + input_data.replace(/\s/g, "_").toLocaleLowerCase(),
                        'text': input_data
                    });
                }
                return array;
            },
            preserveSelected: true
        })
        .change(function() {
            var value = $(this).val();
            if (value) {
                $(this).removeAttr('required');
                $(this).parent().removeClass("is-invalid")
            } else {
                $(this).attr('required', 'required');
                $(this).parent().addClass("is-invalid")
            }
        });
    ajax_select_purpose.trigger('change').data('AjaxBootstrapSelect').list.cache = {}
    if(!ajax_select_office.val()){
        ajax_select_purpose.attr('disabled');
        ajax_select_purpose.siblings().addClass('disabled');
    }

     var checkbox_classes_str = 'input[name^="rating"]'

     var c_classes = checkbox_classes_str.split(',')
     c_classes.forEach(function(class_name, index){
         var instance = $(class_name)
        instance.on('change', function() {
            if ( instance.is(':checked')) {
                instance.removeAttr('required');
                instance.removeClass('is-invalid');
                instance.parent().parent().removeClass('is-invalid');
            } else {
                instance.attr('required', 'required');
                instance.addClass('is-invalid');
                instance.parent().parent().addClass('is-invalid');
            }
        });
     });

     function showRequiredFields(){
         var fields = jQuery('[required]')
         var class_status = 'is-invalid'
         if (!fields.is(':checked')){
            fields.addClass(class_status)
            fields.parent().addClass(class_status)
            fields.parent().parent().addClass(class_status)
         }else {
            fields.removeAttr('required');
            fields.removeClass(class_status)
            fields.parent().removeClass(class_status)
            fields.parent().parent().removeClass(class_status)
         }
     }

     $('button[type="submit"]').click(function (event) {
         showRequiredFields()
     });

     $("form").submit(function(){
         var submit_btn = $('button[type="submit"]');
         var fuid_input = $('input[name="fuid"]');

         if(fuid_input.length === 0){
            submit_btn.text('Unable to submit, reload the page');
            return false;
         }

         fuid_input.val(fuid_value);
         submit_btn.text('Submitting, Please wait');
         submit_btn.attr('disabled', true);
         return true
     });

     showRequiredFields();
});