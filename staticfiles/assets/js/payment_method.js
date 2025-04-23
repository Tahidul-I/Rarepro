$(document).ready(function(){

    $('#pay_online_status').on('click',function(){
        var status = $('#pay_online_status').attr('data-status');
        if(status=="unclicked"){
            //was inactive, making active
            $(this).attr('data-status','clicked');
            $('#pay_cash_status').attr('data-status','unclicked');
            $('#place_order_button').prop('disabled', false);
            $('#payment_method').attr('value','pay_online');
            
        


        }
        else{
            $(this).attr('data-status','unclicked');
            $('#place_order_button').prop('disabled', true);
            alertify.set('notifier','position', 'top-right');
            alertify.error('Please select a payment method');
  
      
            
        }


    });

    $('#pay_cash_status').on('click',function(){
        var status = $('#pay_cash_status').attr('data-status');
      
        if(status=="unclicked"){
            
            $(this).attr('data-status','clicked');
            $('#pay_online_status').attr('data-status','unclicked');
            $('#place_order_button').prop('disabled', false);
            $('#payment_method').attr('value','COD');
       
        }
        else{
            $(this).attr('data-status','unclicked');
            $('#place_order_button').prop('disabled', true);
            alertify.set('notifier','position', 'top-right');
            alertify.error('Please select a payment method');
         
            
        }
    
    });

   
});