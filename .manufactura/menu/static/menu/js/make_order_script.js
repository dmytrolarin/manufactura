$(document).ready(function(){
    var form = $('#modal__form');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        var product_qty = $('#product_qty').val();
        var product_name = $('#product-name').text();

        $('#product_qty').val('1');


        var data = {};
        data.product_name = product_name;
        data.product_qty = product_qty;
        var csrf_token = $('#modal__form [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;
        var url = form.attr('action');

        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
        })

    })
})