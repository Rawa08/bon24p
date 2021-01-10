
$(document).ready(function () {

    $(document).on('submit', '#add_to_cart_form', function (event) {
        event.preventDefault();

        var p_id = $(this).find('#product_id').val()

        var quantity = $(this).find('#product_quantity').val()
        var res = $(this).find('#alert_message')




        $.ajax({
            type: 'POST',
            url: '/cart/add',
            data: { 'post_id': p_id, 'quantity': quantity, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() },


            success: res.removeClass("d-none"),
            error: function (rs, e) {

                console.log(rs.responseText);
            },
        }).done(setInterval(function() {
            res.addClass("d-none")
        }, 2000))
        


    });

    

   
      

})