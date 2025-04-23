$(document).ready(function(){

   
    //Hide Product Size and color name
    $('.choose-size').hide();
    $('.color-name').hide();
    //Hide cart empty message on cart view page
    // $('#cart_empty_message').hide();
    //show size and specifications according to selected color on product detail page
    $('.choose-color').on('click',function(){
        $('.choose-color').removeAttr('id');
        $(this).attr( 'id', 'transform-id' );
        var _color = $(this).attr('data-color');
        $('.choose-size').hide();
        $('.color'+_color).show();
        $('.color'+_color).removeClass('focused-u');
        $('.color'+_color).first().addClass('focused-u');
        var _price = $('.color'+_color).first().attr('data-price');
        $('.product-price').text(_price+" "+"BDT");
        $('.product-price').attr('price-value',_price);
        var _color_name = $('#color-name-'+_color).attr('name');
        $('.spec-color').text(_color_name);
        var _size = $('.color'+_color).first().text();
        $('.spec-size').text(_size);
        $('#color-for-cart').attr('value',  _color_name);
        $('#size-for-cart').attr('value',_size);
        var color = $('#color-for-cart').val();
        var size = $('#size-for-cart').val();
    
        
    
    })

   //show first product size and its price and specifications by default on product detail page
    var _color = $('.choose-color').first().attr('data-color');
    $('.color'+_color).show();
    $('.color'+_color).first().addClass('focused-u');
    $('.choose-color').first().attr( 'id', 'transform-id' );
    var _price = $('.choose-size').first().attr('data-price')
    $('.product-price').text(_price+" "+"BDT");
    $('.product-price').attr('price-value',_price);
    var _color_name = $('.color-name').first().attr('name');
    $('.spec-color').text(_color_name);
    var _size = $('.color'+_color).first().text();
    $('.spec-size').text(_size);
    $('#color-for-cart').attr('value', _color_name);
    $('#size-for-cart').attr('value',_size);
   
    //Show price according to size on product detail page

    $('.choose-size').on('click',function(){
        $('.choose-size').removeClass('focused-u');
        $(this).addClass('focused-u');
        var _price = $(this).attr('data-price');
        $('.product-price').text(_price+" "+"BDT");
        $('.product-price').attr('price-value',_price);
        var _size = $(this).text();
        $('.spec-size').text(_size);
        $('#size-for-cart').attr('value',_size);

    });
    
    
//      //Increasing value of quantity field of product details page

    $('.quantity-increase').on('click',function(){
        var _quantity =parseInt($('#product-quantity').attr('value'))+1;
        $('#product-quantity').attr('value',_quantity);
   
    });

//     //Dicreasing value of quantity field of product details page
    $('.quantity-dicrease').off('click').on('click',function(){
        if(parseInt($('#product-quantity').attr('value'))>1){
            var _quantity =parseInt($('#product-quantity').attr('value'))-1;
            $('#product-quantity').attr('value',_quantity);

        }
   
    });
//    //Increasing Cart quantity in cart view page
   $('.cart-value-increase').off('click').on('click',function(){
    var _data_value = $(this).attr('data-plus');
    console.log(_data_value);
    var _quantity = parseInt($('.cart-'+_data_value).val())+1;
    $('.cart-'+_data_value).val(_quantity);
    
    });

//     //Dicreasing Cart Quantity in cart view page
    $('.cart-value-dicrease').off('click').on('click',function(){
        var _data_value = $(this).attr('data-minus');
        if( parseInt($('.cart-'+_data_value).val())>1){
            var _quantity = parseInt($('.cart-'+_data_value).val())-1;
            $('.cart-'+_data_value).val(_quantity);

        }  ; 
        
    }) ;
   
    
  
    //Add to cart operations(receiving data from product detail page for cart session)

    $(document).on('click','#addToCartBtn',function(event){
        event.preventDefault();
        var _vm = $(this);
        const _productQuantity = $('#product-quantity').val();
        const _productId = $('#product-id').val();
        const _productImage = $('.product-main-image').first().attr('src');
        const _productColor = $('#color-for-cart').val();
        const _productSize = $('#size-for-cart').val();

        $.ajax({
            url:'/add_to_cart',
            data: {
                'product_id':_productId,
                'product_quantity':_productQuantity,
                'product_image':_productImage,
                'product_color':_productColor,
                'product_size':_productSize
            },
            dataType:'json',

            beforeSend:function(){
                _vm.attr('disabled',true);
                
            },
            success:function(response){
                console.log(response.total_cart_items);
                console.log(response.data);
               $('#side-cart-container').html(response.data)
               $('#update_cart_item_number').text(response.total_cart_items);
               
                _vm.attr('disabled',false);
                

            }

        })
       
    })

    // Cart single item delete operations from cart view page

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
                $('body').html(response.data);
                if(parseInt(response.total_cart_items)==0){
                    $('#cart_empty_message').show();
                    $('#clear_cart_button').hide();
                    $('#update_cart_button').hide();
                    $('#proceed_to_checkout_button').hide();
                  
                    
                }
                _vm.attr('disabled', false);

            }
        });
    });

    //Add to cart update operations on cart view page

    $(document).on('click', '#update_cart_button', function () {
        
        var updated_cart_quantity_list = [];
        var csrf_token = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
        $('.cart-quantity-for-update').each(function() {
            var variant_id = parseInt($(this).attr('data-quantity'));
            var changed_quantity = parseInt($('.cart-'+variant_id).val());
            updated_cart_quantity_list.push({'id':variant_id,'quantity':changed_quantity});
        });
        console.log(updated_cart_quantity_list)

        $.ajax({
            url: '/update_cart/',
            type: 'POST',  // Change to POST method
            contentType: 'application/json',
            data: JSON.stringify({ 'updated_cart_quantity_list': updated_cart_quantity_list }),
            headers: {
                'X-CSRFToken': csrf_token
            },  // Stringify the array as JSON
            success: function (response) {
                
                $('body').html(response);
                $('#update_cart_button').attr('type','button');
                $('#update_cart_button').removeAttr('name');
                $('#update_cart_button').removeAttr('value');
                $('#update_cart_button').removeClass('btn-update');
               console.log( $('#update_cart_button').attr('type'));
                
            }
        });
    
    });

    
    $(document).on('click','#place_order_btn',function(){
        var billing_details = {
            'first_name':$('#firstname').val(),
            'last_name':$('#lastname').val(),
            'country':$('#country').val(),
            'address':$('#street-address').val(),
            'city':$('#city').val(),
            'division':$('#division').val(),
            'postal':$('#postcode').val(),
            'phone':$('#phone').val(),
            'email':$('#email').val(),
            'note':$('#order-notes').val(),
        };
        var shipping_details={
            'first_name':$('#shipping-firstname').val(),
            'last_name':$('#shipping-lastname').val(),
            'country':$('#shipping-country').val(),
            'address':$('#shipping-street-address').val(),
            'city':$('#shipping-city').val(),
            'division':$('#shipping-division').val(),
            'postal':$('#shipping-postcode').val(),
            'phone':$('#shipping-phone').val(),
            'email':$('#shipping-email').val(),
            'note':$('#shipping-order-notes').val(),

        };
        var _total_cost = $('#total-cost').text();
        var csrf_token = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
        $.ajax({
            url: '/checkout/',  // Replace with your Django view URL
            type: 'POST',
            data: JSON.stringify({'billing_details':billing_details,'shipping_details':shipping_details,'total_cost':_total_cost}),
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': csrf_token
            }
        });

    });
});