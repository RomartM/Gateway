function boolean_toggle(instance){
    function checkbox(instance){
    let label = 'Yes'
    if(!instance.checked){
        label = 'No'
    }
        instance.parentElement.querySelector(".form-check-label").innerHTML = label
    }
    instance.on("change", function(e){
        checkbox(e.currentTarget)
    })
    instance.map(function(i, e){
        checkbox(e)
    })
}

function add_button(id, label){
    return '<a href="#'+id+'" id="add_'+id+'" class="btn btn-sm btn-primary"><svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+label+'</a>'
}

function div(class_name, body){
    return '<div class="'+class_name+'">'+body+'</div>'
}