from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect,HttpResponse
from manageItems.models import GlobalMenu,Item
from manageStores.models import Restaurant
from manageUsers.models import Customer
from django.contrib.auth.models import User
from .models import Cart, Order
from django.utils import timezone
from addtocart.forms import CartForm



def view_item(request):
    menu = GlobalMenu.objects.get(pk=1)
    latest_item_list = menu.item_set.all()
    res_list = menu.restaurant_set.all()
    context = {
        'latest_item_list': latest_item_list,
        'restaurant_list' : res_list,
    }
    return render(request, 'view_menu.html', context)


def add_to_cart(request):
    if request.method=='GET':
        id = request.GET.get('id')
        menu = GlobalMenu.objects.get(pk=1)
        item = menu.item_set.get(pk=id)
        form_obj = CartForm()
        return render(request, 'edit_cart_item.html', {"form_obj": form_obj,'item': item})
    elif request.method=='POST':
        id = request.GET.get('id')
        menu = GlobalMenu.objects.get(pk=1)
        item = menu.item_set.get(pk=id)
        error_msg = ""
        cart_list = Cart.objects.all().filter(submitted_status__startswith='Un')
        form_obj = CartForm(request.POST)
        if form_obj.is_valid():
            item_qty = form_obj.cleaned_data.get("item_qty")
            if item_qty == 0 :
                form_obj = CartForm()
                res_list = menu.restaurant_set.all()
                error_msg = 'Item Qty must be a positive integer, please enter again!'
                return render(request, 'edit_cart_item.html', {"form_obj": form_obj,'item': item,'error_msg':error_msg})
            else:
                for c in cart_list:
                    if c.item.id == int(id):
                        qty = int(item_qty)
                        c.item_qty = c.item_qty + qty
                        c.save()
                        return HttpResponseRedirect(reverse('iteminfo'))
                status = 'Unsubmitted'
                pubdate = timezone.now()
                cart = Cart(item=item,item_qty=item_qty,submitted_status=status,modify_date=pubdate)
                cart.save()
                return HttpResponseRedirect(reverse('iteminfo'))


def view_cart(request):
    if request.method=='GET':
        sum = 0
        ctx = {}
        latest_item_list = Cart.objects.filter(submitted_status__startswith='Un')
        menu = GlobalMenu.objects.get(pk=1)
        for i in latest_item_list:
            price = int(i.item.item_price)
            qty = int(i.item_qty)
            sum= sum+price*qty

        context = {
            'latest_item_list': latest_item_list,
            'totalPrice':sum,
        }
        return render(request, 'view_cart.html', context)


def create_order(request):
    if request.method=='GET':
        totalPrice = request.GET.get('totalPrice')
        menu = GlobalMenu.objects.get(pk=1)
        res_list = menu.restaurant_set.all()
        context = {
            'totalPrice':totalPrice,
            'restaurant_list':res_list
        }
        return render(request, 'create_order.html',context)
    elif request.method=='POST':
        cust_name = request.POST.get('custname')
        total_price = int(request.POST.get('totalPrice'))
        cart_num = Cart.objects.filter(submitted_status__startswith='Un').count()
        # If the customer name is not empty and the cart has at least one item.
        # Then create a new order.
        if len(cust_name) !=0 and cust_name.isspace() == False and int(cart_num)!=0:

            # Find the customer object through the current log-in user's username
            username = request.session['user_name']
            user = Customer.objects.filter(c_name__exact=username)[0]

            # Get the Restaurant location the customer wants to place an order.
            res = request.POST.get('res')
            restaurant = Restaurant.objects.filter(restauran_location__exact=res)[0]

            # Create an order object
            order = Order.objects.create(user=user, restaurant=restaurant)
            cart_list = Cart.objects.filter(submitted_status__startswith='Un')
            for i in cart_list:
                id = i.id
                order.cart.add(id)
                i.submitted_status='Submitted'
                i.save()
            order.total_price = total_price
            order.customer_name = cust_name
            order.status = 'Awaitting Processing'
            order.modify_date = timezone.now()
            order.save()
            return HttpResponseRedirect(reverse('iteminfo'))
        # If the cart do not have any item(count_num==0), or the customer name is not valid.
        # Display the error message to prompt the customer to select at least one item.
        # Customer can choose the item that has a price of zero.
        else:
            totalPrice=request.POST.get('totalPrice')
            menu = GlobalMenu.objects.get(pk=1)
            res_list = menu.restaurant_set.all()
            context = {
                'totalPrice':totalPrice,
                'restaurant_list':res_list
            }
            if int(cart_num)==0:
                context = {
                    'totalPrice':totalPrice,
                    'restaurant_list':res_list,
                    'error_msg_totalprice' : "Please add at least one item to cart!"
                }
            if len(cust_name) ==0 or cust_name.isspace()==True:
                context = {
                    'totalPrice':totalPrice,
                    'restaurant_list':res_list,
                    'error_msg_customer' : "Customer Name should not be empty!"
                }
            return render(request, 'create_order.html',context)



def remove_from_cart(request):
    if request.method=='GET':
        id = request.GET.get('id')
        cart = Cart.objects.get(pk=id)
        cart.delete()
        return HttpResponseRedirect(reverse('view_cart'))


def view_user_orders(request):
    if request.method=='GET':
        username = request.session['user_name']
        user = Customer.objects.filter(c_name__exact=username)[0]

        latest_item_list = Order.objects.filter(user=user)
        context = {
            'latest_item_list': latest_item_list,
        }
        return render(request, 'view_orders.html',context)

def remove_from_order(request):
    if request.method=='GET':
        id = request.GET.get('id')
        order = Order.objects.get(pk=id)
        order.delete()
        return HttpResponseRedirect(reverse('view_user_orders'))
