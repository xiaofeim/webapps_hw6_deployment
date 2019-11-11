function plus_qty(id) {
    var item_qty_id = "item_qty_" + id;
    var old_qty = parseInt(document.getElementById(item_qty_id).value);
    var new_qty = parseInt(old_qty) + 1;
    $.ajax({
        headers: {
            "X-CSRFToken": $.cookie('csrftoken')
        },
        url: '/handle_qty',
        type: 'POST',
        data: {
            'old_qty': old_qty,
            'new_qty': new_qty,
        },
        success: function (arg) {
            document.getElementById(item_qty_id).value = arg.new_qty;
        },
        error: function () {
            alert("Error")
        }
    });
}

function minus_qty(id) {
    var item_qty_id = "item_qty_" + id;
    var old_qty = parseInt(document.getElementById(item_qty_id).value);
    var new_qty = parseInt(old_qty) - 1;
    if (new_qty < 0 | new_qty == 0) {
        alert("Item Qty cannot less than one.");
        document.getElementById(item_qty_id).value = 1;
    }
    else {
        $.ajax({
            headers: {
                "X-CSRFToken": $.cookie('csrftoken')
            },
            url: '/handle_qty',
            type: 'POST',
            data: {
                'old_qty': old_qty,
                'new_qty': new_qty,
            },
            success: function (arg) {
                document.getElementById(item_qty_id).value = arg.new_qty;
            },
            error: function () {
                alert("Error")
            }
        });
    }
}


function add_to_cart(id, price) {
    var item_qty_id = "item_qty_" + id;
    var item_qty = document.getElementById(item_qty_id).value;
    $.ajax({
        headers: {
            "X-CSRFToken": $.cookie('csrftoken')
        },
        url: '/create_cart',
        type: 'POST',
        data: {
            'item_id': id,
            'item_qty': item_qty,
            'price': price,
        },
        success: function (arg) {
            // alert("Add one item into cart!")
        },
        error: function () {
            alert("Error")
        }
    });
}

function remove_from_cart(obj, id) {
    alert("Hello");
    var index = $(obj).parents("tr").index();
    alert(index);
    var cart_id = id;
    $.ajax({
        headers: {
            "X-CSRFToken": $.cookie('csrftoken')
        },
        url: '/remove_from_cart',
        type: 'POST',
        data: {
            'cart_id': cart_id,
        },
        success: function () {
            $(obj).parents("tr").remove();
        },
        error: function () {
            alert("Error");
        }
    });
}
