

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });
}

function calculateValue() {
    var total = 0;
    $(".product-item").each(function( index ) {
        var qty = parseFloat($(this).find('.product-qty').val());
        var price = parseFloat($(this).find('#product_price').val());
        price = price*qty;
        $(this).find('#item_total').val(price.toFixed(2));
        total += price;
    });
    $("#product_total").val(total.toFixed(2));
}

function orderParser(order) {
    return {
        id : order.id,
        date : order.customerName,
        orderNo : order.customerName,
        customerName : order.customerName,
        cost : parseInt(order.total)
    }
}

function productParser(product) {
    return {
        id : product.id,
        name : product.customerName,
        unit : product.customerName,
        price : product.customerName,
    }
}

function productDropParser(product) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });