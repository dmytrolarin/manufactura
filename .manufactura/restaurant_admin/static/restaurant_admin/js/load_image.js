const fil = document.getElementById('file_id');
if(fil !== null){
    fil.addEventListener('change', function(){
        if(this.files && this.files[0]){
            var reader = new FileReader();
            reader.onload = function(e){
                document.getElementById('image_id').setAttribute('src', e.target.result);
            };
            reader.readAsDataURL(this.files[0]);
        }
    });
}