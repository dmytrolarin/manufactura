// $(document).ready(function(){
    
//     form =  $("#form-buying-product");
//     form.on('submit', function(e){
//         e.preventDefault();
//         var product_amount = $('#product_amount').val();
//         var submit_btn = $('.btn-buy');
//         var product_name = submit_btn.data('product-name');
//         var product_price = submit_btn.data('product-price');
//         var product_slug = submit_btn.data('product-slug');


//             var data = {};
//             data.product_name = product_name
//             data.product_price = product_price
//             data.product_amount = product_amount
//             data.product_slug = product_slug
//             var csrf_token = $('#form-buying-product [name="csrfmiddlewaretoken"]').val();
//             data['csrfmiddlewaretoken'] =  csrf_token;
//             var url = form.attr('action');
//             $.ajax({
//                 url:url,
//                 type: 'POST',
//                 data:data,
//                 cache:true,
//                 success: function (data){
//                     console.log(product_name, product_price, product_amount,'шт.');
//                 },
//                 error: function(){
//                     console.log('error')
//                 }
//             })


        
//     });
    
    // forms = Array.from($(".form-buying-product"));
    // $.each(forms,function(index,form){
    //     console.log(forms);
        // form.on('submit', function(e){
        //     e.preventDefault();
        //     var pr_amount = $('#product_amount').val();
        //     var submit_btn = $('.btn-buy');
        //     var product_name = submit_btn.data('product-name');
        //     var product_price = submit_btn.data('product-price');
        //     console.log(product_name, product_price, pr_amount,'шт.');
        // });
       
        
      
// });
    

