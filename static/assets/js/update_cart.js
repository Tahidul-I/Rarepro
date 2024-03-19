
$(document).ready(function(){

     //Add to cart update operations on cart view page

     $(document).on('click', '#update_cart_button', function () {
        
        var updated_cart_quantity_list = [];
        var csrf_token = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
        $('.cart-quantity-for-update').each(function() {
            var variant_id = parseInt($(this).attr('data-quantity'));
            var changed_quantity = parseInt($('.cart-'+variant_id).val());
            updated_cart_quantity_list.push({'id':variant_id,'quantity':changed_quantity});
        });

        $.ajax({
            url: '/update_cart/',
            type: 'POST',  // Change to POST method
            contentType: 'application/json',
            data: JSON.stringify({ 'updated_cart_quantity_list': updated_cart_quantity_list }),
            headers: {
                'X-CSRFToken': csrf_token
            },  // Stringify the array as JSON
            success: function (response) {
                
                $('#table-container_data').html(response.data);
                $('#cart_total_amount').text('BDT'+" "+response.total_amount);
                $('#updated-total-amount').text('BDT'+" "+response.total_amount);
                $('#update_cart_button').attr('type','button');
                
            }
        });
    
    });

})