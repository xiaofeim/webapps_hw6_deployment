from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from manageItems.models import GlobalMenu,Item
from manageStores.models import Restaurant
from addtocart.models import Cart, Order
from django.utils import timezone
from django import forms
from manageOrders.forms import OrderForm
from manageUsers.models import Employee,Manager


def view_orders(request):
    if request.method=='GET':
        order_list = Order.objects.all().order_by('id')
        order_selected = []
        location_selected = []
        work_location = []
        manager_list = Manager.objects.all()
        employee_list = Employee.objects.all()
        username = request.session['user_name']
        # Get the current manager or employee's working location list.
        for m in manager_list:
            if m.manager.username == username:
                work_location = m.restaurant.all()
        for e in employee_list:
            if e.employee.username == username:
                work_location = e.restaurant.all()
        for w in work_location:
            location_selected.append(w.restauran_location)
        # Get the orders' restaurant location
        for o in order_list:
            if o.restaurant.restauran_location in location_selected:
                order_selected.append(o)
        context = {
            'latest_item_list': order_selected,
        }
        return render(request, 'view_submitted_orders.html',context)

# Change the customer name and order status through order id.
def edit_submitted_orders(request):
    if request.method=='GET':
        order_id = request.GET.get('id')
        order = Order.objects.get(id=order_id)
        form_obj = OrderForm(instance = order)
        return render(request, 'fulfill_orders.html',{'order': order, "form_obj":form_obj})
    elif request.method == "POST":
        
        order_id = request.GET.get('id')
        order = Order.objects.get(id=order_id)
        form_obj = OrderForm(request.POST,instance = order)
        if form_obj.is_valid():
            order.modify_date = timezone.now()
            form_obj.save()
        return HttpResponseRedirect(reverse('orderinfo'))

def delete_submitted_orders(request):
    order_id = request.GET.get('id')
    order = Order.objects.get(id=order_id)
    order.delete()
    return HttpResponseRedirect(reverse('orderinfo'))