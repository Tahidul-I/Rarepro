$(document).ready(function(){

      
        var selected_material = $('#material_type option:selected');
        var material_id = selected_material.val();
        $('.material'+material_id).show();
        $('.material'+material_id).first().attr('selected','selected')
        var _price = parseInt($('#dimension option:selected').attr('data-price'));
        $('#product_price_field').text("BDT"+" "+_price);
        $('#spec-dimension').text( $('.material'+material_id).attr('data-title'));
        $('#spec-material').text(selected_material.attr('material-name'));
       

     //Increasing value of quantity field of product detail page
    
        $('.quantity-increase').on('click',function(){
            var _quantity =parseInt($('#product-quantity').attr('value'))+1;
            $('#product-quantity').attr('value',_quantity);
       
        });
    
    //     //Dicreasing value of quantity field of product detail page
        $('.quantity-dicrease').off('click').on('click',function(){
            if(parseInt($('#product-quantity').attr('value'))>1){
                var _quantity =parseInt($('#product-quantity').attr('value'))-1;
                $('#product-quantity').attr('value',_quantity);
    
            }
       
        });
        $(document).on('change','#dimension',function(){
            var selected_dimension = $(this).find('option:selected');
            var _price = parseInt(selected_dimension.attr('data-price'));
            $('#product_price_field').text("BDT"+" "+_price);
            $('#spec-dimension').text(selected_dimension.attr('data-title'));
            
           
        });
    
        $(document).on('change','#material_type',function(){
            console.log($(this).val());
            $('.material-dimension').hide();
            $('.material-dimension').removeAttr('selected');
            var selected_material = $(this).find('option:selected');
            var _material_id =  selected_material.val();
            $('.material'+_material_id).show();
            $('.material'+_material_id).first().attr('selected','selected');
            var _price =  parseInt($('.material'+_material_id).first().attr('data-price'));
            $('#product_price_field').text("BDT"+" "+_price);
            $('#spec-dimension').text($('.material'+_material_id).first().attr('data-title'));
            $('#spec-material').text(selected_material.attr('material-name'));
            
        
        });
})