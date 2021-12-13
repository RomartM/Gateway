function revive_existing_files(instance, id){
    let select_field = jQuery("select#id_"+id+" option:selected")
    let opt;
    let file_uuid
    for(opt=0; opt<select_field.length; opt++){
        file_uuid = select_field[opt].value
        if(file_uuid){
            try{
                $.ajax({
                type: 'GET',
                url: '/media-manager/get/' + file_uuid,
                success: function(result){
                    if(result.thumbnail){
                        let mockFile = { name: result.name, size: result.bytes, accepted: true };
                        instance.displayExistingFile(mockFile, result.thumbnail)
                        $("#id_"+id+"-files").append('<input type="hidden" name="'+id+'" id="id_'+id+'_'+file_uuid+'" value="'+file_uuid+'" >')
                        $(mockFile.previewElement).attr("server-id", file_uuid);
                    }
                }
            });
            }catch (e) {
                alert("We're unable to retrieve existing selected files, Please try to refresh the page")
            }
        }
    }

    return instance
}

function dropzone_config(id, max_files, form_params){

    return {
        url: window.media_config.base + 'upload/',
        paramName: "file",
        params: form_params,
        addRemoveLinks: true,
        maxFiles: max_files,
        init: function() {
            // Revive existing files
            let instance = this
            instance.on("success", function(file, response) {
                console.log(response)
                try {
                    $("#id_"+id+"-files").append('<input type="hidden" name="'+id+'" id="id_'+id+'_'+response.uuid+'" value="'+response.uuid+'" >')
                    $(file.previewElement).attr("server-id", response.uuid);
                } catch (err) {
                    this.removeFile(file);
                    alert("Something went wrong uploading the content")
                }
            })
             instance.on("error", function(file, response) {
                this.removeFile(file);
                alert(response.errors)
            })
            instance.on("maxfilesexceeded", function(file) {
                alert("Maximum number of files reached: Maximum of "+max_files+ " files are allowed.");
                this.removeFile(file);
            });
            revive_existing_files(instance, id)
        },
        removedfile: function(file) {
            let file_id = $(file.previewElement).attr("server-id")
            if (file_id) {
                $("#id_"+id+"_" + file_id).remove();
                $.ajax({
                    type: 'DELETE',
                    url: window.media_config.base + 'delete/',
                    data: {
                        "csrfmiddlewaretoken": window.form_params.csrfmiddlewaretoken,
                        "uuid": $(file.previewElement).attr("server-id")
                    }
                });
            }
            var _ref;
            return (_ref = file.previewElement) != null ? _ref.parentNode.removeChild(file.previewElement) : void 0;
        }
    }
}

function template(id, message){
    return '<div id="id_'+id+'-files"></div>' +
        '<div class="dropzone dropzone-file-area" id="fileUpload_'+id+'">' +
        '<div class="dz-default dz-message">' +
        '<h3 class="sbold">Drop files here to upload</h3>' +
        '<span>'+message+'</span>' +
        '</div></div>'
}