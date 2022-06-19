$(document).ready(function(){
    form = $('#form-buying-product');
    console.log(form)
    form.on('submit', function(e){
        e.preventDefault();
        var pr_amount = $('#product_amount').val();
        var submit_btn = $('.btn-buy');
        var product_name = submit_btn.data('product-name');
        var product_price = submit_btn.data('product-price');
        console.log(product_name, product_price, pr_amount,'шт.');
    })
})
