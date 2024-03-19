$(document).ready(function () {
    var hover_element = $('.hover-control');
    hover_element.hover(
        function () {
            // This function is called on mouseenter
            $('#category-dropdown-box').show();
            $('#category-dropdown-button').css({
                'color': 'white',
                'background-color': '#1a6985'
            });
        },
        function () {
            // This function is called on mouseleave
            $('#category-dropdown-box').hide();
            $('#category-dropdown-button').removeAttr('style');
        }
    );

    $('.side_bar_cart_menu').on('click',function(){
        alertify.set('notifier','position', 'top-center');
        alertify.error('You have no item in your cart');
    });




});