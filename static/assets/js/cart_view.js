$(document).ready(function(){


    //Increasing Cart quantity in cart view page
   $('.cart-value-increase').off('click').on('click',function(){
    var _data_value = $(this).attr('data-plus');
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
    $(document).on('click', '.updated-cart-value-increase', function(){
        // Your code for increase button
        var _data_value = $(this).attr('data-plus');
        var _quantity = parseInt($('.cart-'+_data_value).val())+1;
        $('.cart-'+_data_value).val(_quantity);
    });
    $(document).on('click', '.updated-cart-value-dicrease', function(){
        // Your code for increase button
        var _data_value = $(this).attr('data-minus');
        if( parseInt($('.cart-'+_data_value).val())>1){
            var _quantity = parseInt($('.cart-'+_data_value).val())-1;
            $('.cart-'+_data_value).val(_quantity);

        }  ;
    });
    // $('.updated-cart-value-increase').off('click').on('click',function(){
    //     console.log("clicked");
    //     var _data_value = $(this).attr('data-plus');
    //     console.log(_data_value);
    //     var _quantity = parseInt($('.cart-'+_data_value).val())+1;
    //     $('.cart-'+_data_value).val(_quantity);
        
    //     });

        $('.updated-cart-value-dicrease').off('click').on('click',function(){
            var _data_value = $(this).attr('data-minus');
            if( parseInt($('.cart-'+_data_value).val())>1){
                var _quantity = parseInt($('.cart-'+_data_value).val())-1;
                $('.cart-'+_data_value).val(_quantity);
    
            }  ; 
            
        }) ;

    

});