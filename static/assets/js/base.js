$(document).ready(function(){
    
    $('.base_side_bar_cart_menu').on('click',function(){
        console.log("I ahve been clicked");
        alertify.set('notifier','position', 'top-center');
        alertify.error('You have no item in your cart');
    });

});