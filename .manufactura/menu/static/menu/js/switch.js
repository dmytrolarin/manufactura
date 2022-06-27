$(document).ready(function(){
    $('.increment_btn').click(function(e){
        e.preventDefault();
        var inc_value = $(this).closest('.list').find('.form_control').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        if(value < 10){
            value++;
            $(this).closest('.list').find('.form_control').val(value);
        }
    });
    $('.decrement_btn').click(function(e){
        e.preventDefault();
        var dec_value = $(this).closest('.list').find('.form_control').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if(value > 1){
            value--;
            $(this).closest('.list').find('.form_control').val(value);
        }
    });
});
