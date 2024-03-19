$(document).ready(function(){
    var filter_object = {};
    var num_of_products = $('#products_per_page').attr('data-limit');
    $('.filter-checkbox').on('click',function(){

        var filter_key = $(this).attr('data-key');
        if(filter_key == "price"){
            var status = $(this).attr('price-data-status');
            if(status=="inactive"){
                $(this).attr('price-data-status','active');
            }
            else{
                $(this).attr('price-data-status','inactive');
    
            }
        }
        else{
            var status = $(this).attr('brand-data-status');
            if(status=="inactive"){
                $(this).attr('brand-data-status','active');
            }
            else{
                $(this).attr('brand-data-status','inactive');
               
            }
        }
      
    });

    $('.filter-checkbox').on('click',function(){
        
        var csrf_token = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
        var filter_key = $(this).attr('data-key');
        if(filter_key == "price"){

            var elements = document.querySelectorAll('[price-data-status="active"]');
            var valuesArray_Max = Array.from(elements).map(function(element) {
                return parseInt(element.getAttribute('data-max-value'));

            });
            filter_object['max'] = valuesArray_Max;
            
            var valuesArray_Min = Array.from(elements).map(function(element) {
                return parseInt(element.getAttribute('data-min-value'));

            });
            filter_object['min'] = valuesArray_Min;
      
        }
        else{
            var elements = document.querySelectorAll('[brand-data-status="active"]');
            var valuesArray = Array.from(elements).map(function(element) {
                return parseInt(element.getAttribute('data-value'));
    
            });

            filter_object['brand'] = valuesArray;
      

        }
  
        var category = $('#product_category_filter').text();
        
        $.ajax({
            url: '/product_filter/',
            type: 'POST',  // Change to POST method
            contentType: 'application/json',
            data: JSON.stringify({ 'filter_object': filter_object,'category':category,'num_of_products':num_of_products}),
            headers: {
                'X-CSRFToken': csrf_token
            },  // Stringify the array as JSON
            success: function (response) {

                if (response.redirect_url) {
                    // Redirect to the URL received in the JSON response
                    console.log("The redirect url is here ");
                    window.location.href = response.redirect_url;
                }

                else{
                    $('#product_main_section').html(response.product_template);
                    $('#pagination_box').html(response.pagination);
                }
                
            }
        });

       
    });
});