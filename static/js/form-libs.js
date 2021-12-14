// Checkbox
let instance = jQuery('[type="checkbox"]')
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