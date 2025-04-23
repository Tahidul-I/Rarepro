$(document).ready(function(){
     

     //Add to cart operations(receiving data from product detail page for cart session)

     $(document).on('click','#addToCartBtn',function(event){
        event.preventDefault();
        var _vm = $(this);
        console.log("I am here");
        var selected_material = $('#material_type option:selected');
        var selected_dmension  = $('#dimension option:selected') ;
        const _productQuantity = $('#product-quantity').val();
        const _productId = $('#product-id').val();
        const _productImage = $('.product-main-image').first().attr('src');
        const _material_type = selected_material .text();
        const _dimension = selected_dmension.text();
        
        $.ajax({
            url:'/add_to_cart',
            data: {
                'product_id':_productId,
                'product_quantity':_productQuantity,
                'product_image':_productImage,
                'material_type':_material_type,
                'dimension': _dimension
            },
            dataType:'json',

            beforeSend:function(){
                _vm.attr('disabled',true);
                
            },
            success:function(response){
               $('#side-cart-container').html(response.sidebar_template);
               $('#product_detail_page_sidebar_cart_action').html(response.sidbar_cart_action_template);
               $('#update_cart_item_number').text(response.total_cart_items);
               
                _vm.attr('disabled',false);
                

            }

        })
       
    })

});