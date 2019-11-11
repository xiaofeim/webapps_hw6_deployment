

// $(document).ready(function () {
//     setInterval("updateOrders()",15000);
// });
// function updateOrders()
// {
//     alert("Hello");
//     var username = document.getElementById("session").value;
//     $.ajax({
//         headers: {
//             "X-CSRFToken":$.cookie('csrftoken')
//         },
//         url: '/update_orders',
//         type: 'POST',
//         data:{
//             'user_name': username,
//         },
//         success: function (arg) {
//             var order_lists = JSON.parse(arg.order);
//             var count = arg.count;
//             for(var i=0; i<count; i++){
//                 var orderId = order_lists[i].pk;
//                 // var cart = order_lists[i].fields.cart;
//                 var totalPrice = order_lists[i].fields.total_price;
//                 var cusName = order_lists[i].fields.customer_name;
//                 var status  = order_lists[i].fields.status;
//                 var date = order_lists[i].fields.modify_date;
//                 // getCart(order_lists[i]);
                
//                 // alert(totalPrice)
//                 // alert(cusName)
//                 // alert(status)
//                 // alert(date)
//                 document.getElementById("order_"+orderId).value = orderId;
//                 alert(document.getElementById("order_"+orderId).value)
//                 // document.getElementById("order_tp_"+orderId).value = totalPrice;
//                 // document.getElementById("order_cn_"+orderId).value = cusName;
//                 // document.getElementById("order_date_"+orderId).value = date;
//                 // document.getElementById("order_date_"+orderId).value = status;
//             }
//         },
//         error: function () {
//             alert("Error")
//         }
//     });
// }

// // function getCart(order){
// //     var cartId_list = order.fields.cart;
// //     alert(cartId_list);
// //     $.ajax({
// //         headers: {
// //             "X-CSRFToken":$.cookie('csrftoken')
// //         },
// //         url: '/get_cart',
// //         type: 'POST',
// //         data:{
// //             'cart_list': cartId_list,
// //         },
// //         success: function (arg) {
// //             alert("Hello");
// //         },
// //         error: function () {
// //             alert("Error");
// //         }
// //     });

    
// // }