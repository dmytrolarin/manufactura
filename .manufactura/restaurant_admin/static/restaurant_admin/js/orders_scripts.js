// $(document).ready(function(){
    
//     $(document).on('click','.enter', function(e){

//         e.preventDefault();
//         var order_pk = $(this).closest('.form_enter').find('.order_pk').val();
//         var order_format = $(this).closest('.form_enter').find('.order_format').val();
        
//         var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
       
//         var data = {};
//         data.order_pk = order_pk;
//         data.order_format = order_format;
//         data['csrfmiddlewaretoken'] = csrf_token;
        
//         var url = $(this).closest('.form_enter').find('.set_order_active_status').val();

//         console.log(url)
//         $.ajax({
//             url:url,
//             type:'POST',
//             data:data,
//             cache:true,
//             success: function(){

//                $(this).closest('.block-form-reservation').load(location.href + '  block-form-reservation')
//             }
//         })
     
//     });
   
    
// });
