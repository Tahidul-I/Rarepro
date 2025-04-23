$(document).ready(function(e){
    $('#cinfirm_alert_container').hide();
    $(document).on('click','#place_order_button',function(){
        var payment_mode = $('#payment_method').attr('value');
        if (payment_mode=="pay_online"){
            alertify.confirm('Are you sure? ', 'Pressing Ok will take you to the online payment procedure', function(){ 
                document.getElementById('checkout_detail_form').submit();
             }
        , function(){ });
        }
        else{
            alertify.confirm('Are you sure? ', 'Pressing Ok will place your order which can not be cancelled', function(){ 
                document.getElementById('checkout_detail_form').submit();
             }
            , function(){ });
        }
        
    });

   
    
});


