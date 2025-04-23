$(document).ready(function(){

    $(document).on('click','#apply-coupon-btn',function(){
        var coupon_code =$('#coupon_code').val();
        var total_cost = $('#total-cost').text();
        var subtotal_amount = $('#subtotal-amount').text();
        var _vm = $(this);
        console.log(coupon_code);
        console.log(total_cost);

        $.ajax({
            url:'/coupon_discount',
            data:{
                'coupon_code':coupon_code,
                'total_cost':total_cost,
                'subtotal_amount':subtotal_amount
            },
            dataType:'json',
            beforeSend:function(){
                _vm.attr('disabled',true);
                
            },
            success:function(response){
                _vm.attr('disabled',false);

                if (response.total_amount!=0){
                    $('#total-cost').text(response.total_amount);
                    $('#discounted-amount').text(response.discounted_amount);

                }
                else{
                    $.getScript('https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/js/toastr.min.js', function() {
                    toastr.error('Invalid Coupon');
                     });
                }


                
                

            }
        });
    });



})