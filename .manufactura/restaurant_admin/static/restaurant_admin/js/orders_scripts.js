setTimeout(function(){
    location.reload();
}, 300000);

$(document).ready(function(){
    
    $(document).on('click','.btn_modal', function(e){
        
        var cancel_reason = document.getElementById('cancel-reason').value;
        var order_pk = document.getElementById('order_pk').value;
        var order_format = document.getElementById('order_format').value;
        var new_status = document.getElementById('new_status').value;
        var func_abs_url = document.getElementById('func_abs_url').innerText;
        var csrf_token = $('input[name=csrfmiddlewaretoken]').val   ();
        
       
        var data = {};
        data.order_pk = order_pk;
        data.cancel_reason = cancel_reason;
        data.order_format = order_format;
        data.new_status = new_status;
        data['csrfmiddlewaretoken'] = csrf_token;
        var url = func_abs_url;

        console.log(url)
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,

        })
     
    });
   
    
});
