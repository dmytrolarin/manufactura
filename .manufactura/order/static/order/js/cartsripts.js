$(document).ready(function(){
    $(document).on('click','.increment_btn', function(e){
        e.preventDefault();
        var inc_value = $(this).closest('.block-cart__product').find('.form_control').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
     
        if(value < 10){
            value++;
            $(this).closest('.block-cart__product ').find('.form_control').val(value);
            
        }
    });
    $(document).on('click','.decrement_btn', function(e){
        e.preventDefault();
        var dec_value = $(this).closest('.block-cart__product').find('.form_control').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if(value > 1){
            value--;
            $(this).closest('.block-cart__product').find('.form_control').val(value);
        }
    });

    $(document).on('click','.changeQuantity', function(e){
        console.log(1);
        e.preventDefault();
        var product_name = $(this).closest('.block-cart__product').find('.product__name').text();
        var product_qty = $(this).closest('.block-cart__product').find('.qty-input').val();
        var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        
        var data = {};
        data.product_name = product_name;
        data.product_qty = product_qty;
        data['csrfmiddlewaretoken'] = csrf_token;
        
        var url = $(this).closest('.block-cart__product').find('.url_update_cart').val();
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(){
                // $('.form-data').load(location.href + '  .form-data');

                $('.total-price-data').load(location.href + '  .total-price-data')
            }
        })
     
    });
    $(document).on('click','.product__delete', function(e){

        e.preventDefault(); 
        var product_name = $(this).closest('.block-cart__product').find('.product__name').text();
        var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        
        var data = {};
        data.product_name = product_name;
        data['csrfmiddlewaretoken'] = csrf_token;
        
        var url = $(this).closest('.block-cart__product').find('.url_delete_cart').val();
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(){
                $('.card-data').load(location.href + '  .card-data');
                $('.total-price-data').load(location.href + '  .total-price-data'); 
            }
        });
     
    });



    // $(document).on('click','.changeQuantity', function(e){
    //     e.preventDefault();
    //     var product_name = $(this).closest('.block-cart__product').find('.product__name').text();
    //     var product_qty = $(this).closest('.block-cart__product').find('.qty-input').val();
    //     var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        
    //     var data = {};
    //     data.product_name = product_name;
    //     data.product_qty = product_qty;
    //     data['csrfmiddlewaretoken'] = csrf_token;
        
    //     var url = $(this).closest('.block-cart__product').find('.url_update_cart').val();
    //     $.ajax({
    //         url:url,
    //         type:'POST',
    //         data:data,
    //         cache:true,
    //         success: function(){
    //             $('.total-price-data').load(location.href + '  .total-price-data');
    //             // $('.card-data').load(location.href + '  .card-data');
    //         }
    //     })
     
    // });
    // $(document).on('click','.product__delete', function(e){

    //     e.preventDefault(); 
    //     var product_name = $(this).closest('.block-cart__product').find('.product__name').text();
    //     var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        
    //     var data = {};
    //     data.product_name = product_name;
    //     data['csrfmiddlewaretoken'] = csrf_token;
        
    //     var url = $(this).closest('.block-cart__product').find('.url_delete_cart').val();
    //     $.ajax({
    //         url:url,
    //         type:'POST',
    //         data:data,
    //         cache:true,
    //         success: function(){
    //             $('.card-data').load(location.href + '  .card-data');
    //             
    //         }
    //     });
     
    // });

    
});
