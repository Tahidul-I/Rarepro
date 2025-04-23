
$(document).ready(function(){


    $(document).on('click', '.delete-icon', function() {
        var _vm = $(this);
        var _product_variant_id = $(this).attr('id');
        $('.table-row-'+_product_variant_id).remove();
    
        $.ajax({
            url: '/delete_cart_single_item',
            data: {
                'product_variant_id': _product_variant_id,
            },
            dataType: 'json',  // Corrected: Added space after dataType
            beforeSend: function() {  // Corrected: Changed to beforeSend
                _vm.attr('disabled', true);
            },
            success: function(response) {
                $('#side-cart-container').html(response.data);
                $('#cart_total_amount').text("BDT"+" "+response.total_amount);
                $('#update_cart_item_number').text(response.total_cart_items);
                $('#updated-total-amount').text("BDT"+" "+response.total_amount);
                if(parseInt(response.total_cart_items)==0){
                    $('#cart_empty_message').show();
                   $('.hide-button').hide();
                  
                    
                }
                _vm.attr('disabled', false);

            }
        });
    });

    
})