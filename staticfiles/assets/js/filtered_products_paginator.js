$(document).ready(function(){
    
    var checked_items = {};
    $(document).on('click','.pagination_link',function(event){
        
    
        $('.pagination_box').removeClass('active');
        $(this).parent().addClass('active');
        console.log($(this).parent().attr('class'));
        var category = $('#product_category_filter').text();
        var products_per_page = $('#products_per_page').attr('data-limit');
        var page_number = $(this).attr('data-page');
        var csrf_token = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
        //Filtering out which price ranges were checked and their corresponding price rages values
        var price_elements = document.querySelectorAll('[price-data-status="active"]');
        var valuesArray_Max = Array.from(price_elements).map(function(element) {
            return parseInt(element.getAttribute('data-max-value'));

        });

        checked_items['max'] = valuesArray_Max;
            
        var valuesArray_Min = Array.from(price_elements).map(function(element) {
            return parseInt(element.getAttribute('data-min-value'));

        });
        checked_items['min'] = valuesArray_Min;

        // Filtering out the all btand id that are selected

        var brand_elements = document.querySelectorAll('[brand-data-status="active"]');
        var valuesArray = Array.from(brand_elements).map(function(element) {
            return parseInt(element.getAttribute('data-value'));

        });

        checked_items['brand'] = valuesArray;

        $.ajax({
            url: '/filtered_product_paginator/',
            type: 'POST',  // Change to POST method
            contentType: 'application/json',
            data: JSON.stringify({ 'checked_items': checked_items,'category':category,'products_per_page':products_per_page,'page_number':page_number}),
            headers: {
                'X-CSRFToken': csrf_token
            },  // Stringify the array as JSON
            success: function (response) {

                $('#product_main_section').html(response.product_template);
           
                
            }
        });
        
        event.preventDefault();
    });
        
        

       
 
});