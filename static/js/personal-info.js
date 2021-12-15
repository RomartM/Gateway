// Indigenous Checkbox
let instance = jQuery('#id_has_indigenous_group');
let id_indigenous_group_label = jQuery('[for="id_indigenous_group"]')
let id_indigenous_group = jQuery('#id_indigenous_group');
let id_other_indigenous_group_label = jQuery('[for="id_other_indigenous_group"]')
let id_other_indigenous_group = jQuery('#id_other_indigenous_group');

function indigenous_checkbox(instance){
    if(!instance.checked){
        id_indigenous_group_label.hide()
        id_indigenous_group.hide()
        id_other_indigenous_group_label.hide()
        id_other_indigenous_group.hide()
        id_other_indigenous_group_label.removeClass("required")
        id_other_indigenous_group.removeAttr("required")
    }else{
        id_indigenous_group_label.show()
        id_indigenous_group.show()
        indigenous_select()
    }
}
function indigenous_select(){
    if(id_indigenous_group.val() === '1'){
        id_other_indigenous_group_label.show()
        id_other_indigenous_group.show()
        id_other_indigenous_group_label.addClass("required")
        id_other_indigenous_group.attr("required", true)
    }else{
        id_other_indigenous_group_label.hide()
        id_other_indigenous_group.hide()
        id_other_indigenous_group_label.removeClass("required")
        id_other_indigenous_group.removeAttr("required")
    }
}
function indigenous_field_init(){
    instance.map(function(i, e){
        indigenous_checkbox(e)
    })
    instance.on("click", function(e){
        indigenous_checkbox(e.currentTarget)
    })
    id_indigenous_group.on("click", function(e){
        indigenous_select()
    })
    indigenous_select()
}
indigenous_field_init()


// Boolean Toggle
let boolean_toggles = jQuery('#id_has_indigenous_group, #id_dual_citizenship, #id_by_birth, #id_by_naturalization')
boolean_toggle(boolean_toggles)


// Address Field
let id_address = jQuery('#id_address')

function address_init(){
    var _field = 'address'
    id_address.addClass('ghost')
    id_address.before(add_button(_field, 'Add Address'))

    var add_btn_instance = jQuery("#add_"+_field)
    add_btn_instance.after(div('mb-3', ''))
}
address_init()