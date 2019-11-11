from django.shortcuts import render,HttpResponse,reverse
from django.http import HttpResponseRedirect
from django import forms
from .forms import ItemForm
from .models import GlobalMenu,Item
from addtocart.models import Cart, Order
from manageUsers.models import Employee,Manager
from manageStores.models import Restaurant
import json
from django.utils import timezone
from django.core import serializers



def open_dashboard(request):
    return render(request,'dashboard.html')

def handle_qty(request):
    old_qty = request.POST['old_qty']
    new_qty = request.POST['new_qty']
    data={
        'old_qty':old_qty,
        'new_qty': new_qty,
    }
    return HttpResponse(json.dumps(data),content_type="application/json")

def create_cart(request):
    item_qty = int(request.POST['item_qty'])
    item_price = request.POST['price']
    item_id = request.POST['item_id']
    menu = GlobalMenu.objects.get(pk=1)
    item = menu.item_set.get(pk=item_id)
    data={}
    cart_list = Cart.objects.all().filter(submitted_status__startswith='Un')
    for c in cart_list:
        if c.item.id == int(item_id):
            qty = int(item_qty)
            c.item_qty = c.item_qty + qty
            c.save()
            return HttpResponse(json.dumps(data),content_type="application/json")
    # Create a new cart object
    status = 'Unsubmitted'
    pubdate = timezone.now()
    cart = Cart(item=item,item_qty=item_qty,submitted_status=status,modify_date=pubdate)
    cart.save()
    return HttpResponse(json.dumps(data),content_type="application/json")

def update_orders(request):
    username = request.POST['user_name']
    old_list = json.loads(request.POST['order_id_list'])
    new_list = []
    order_list = Order.objects.all().order_by('id')
    order_selected = []
    location_selected = []
    count = 0
    item_count = 0
    qty_count = 0
    res_list = []
    item_list = []
    qty_list = []
    manager_list = Manager.objects.all()
    employee_list = Employee.objects.all()
    for m in manager_list:
        if m.manager.username == username:
            work_location = m.restaurant.all()
    for e in employee_list:
        if e.employee.username == username:
            work_location = e.restaurant.all()
    for w in work_location:
        location_selected.append(w.restauran_location)
    for o in order_list:
        if o.restaurant.restauran_location in location_selected:
            order_selected.append(o)
    # If the order is in order_selected but not in order_id_list
    # The order is new and it should be append to the page
    for o in order_selected:
        if o.id in old_list:
            continue
        else:
            new_list.append(o)
            count = count+1
            res_list.append(o.restaurant.restauran_location)
            for c in o.cart.all():
                item_list.append(c.item.item_name)
                qty_list.append(c.item_qty)
                item_count= item_count+1
                qty_count = qty_count+1
    new_list = serializers.serialize('json',new_list)
    data={
        'user_name':username,
        'order_lists':new_list,
        'res_list': res_list,
        'item_list': item_list,
        'qty_list': qty_list,
        'count': count,
        'item_count': item_count,
        'qty_count': qty_count
    }
    return HttpResponse(json.dumps(data),content_type="application/json")

def get_res(request):
    res_Id = int(request.POST['res_Id'])
    res = Restaurant.objects.get(id=res_Id)
    location = res.restauran_location
    data={
        'res': location
    }
    return HttpResponse(json.dumps(data),content_type="application/json")


def remove_from_cart(request):
    cart_id = int(request.POST['cart_id'])
    cart = Cart.objects.get(pk=cart_id)
    data={}
    return HttpResponse(json.dumps(data),content_type="application/json")

def get_cart(request):
    cartId_list = request.POST['cart_list']
    data = {}
    for c in cartId_list:
        print(c)
        return HttpResponse(json.dumps(data),content_type="application/json")


def view_all_items(request):
    menu = GlobalMenu.objects.get(pk=1)
    latest_item_list = menu.item_set.all().order_by('id')
    context = {
        'latest_item_list': latest_item_list,
    }
    return render(request, 'view_all_items.html',context)


# When create a new item, the item_price could be zero, as it may be a business promotion. 
def add_iteminfo(request):
   
    if request.method == "GET":
        form_obj = ItemForm()
        return render(request,'add_item.html',{"form_obj": form_obj})
    elif request.method == "POST":
        form_obj = ItemForm(request.POST, request.FILES)
        if form_obj.is_valid():
            global_menu = form_obj.cleaned_data.get("global_menu")
            item_name = form_obj.cleaned_data.get("item_name")
            item_price = form_obj.cleaned_data.get("item_price")
            item_description = form_obj.cleaned_data.get("item_description")
            file_obj = form_obj.cleaned_data.get('item_img')
            global_menu.item_set.create(global_menu = global_menu, item_name=item_name,item_description=item_description,item_price=item_price,item_img = file_obj)
            return HttpResponseRedirect(reverse('menuinfo'))

def edit_iteminfo(request):
    
    if request.method=="GET":
        id = request.GET.get('id')
        menu = GlobalMenu.objects.get(pk=1)
        item = menu.item_set.get(pk=id)
        form_obj = ItemForm(instance = item)
        return render(request, 'edit_item.html',{"form_obj": form_obj,'item':item})
    elif request.method == "POST":
        id = request.GET.get('id')
        menu = GlobalMenu.objects.get(pk=1)
        item = menu.item_set.get(id=id)
        form_obj = ItemForm(request.POST, request.FILES,instance=item)
        if form_obj.is_valid():
            form_obj.save()                   
            return HttpResponseRedirect(reverse('menuinfo'))

def delete_iteminfo(request):
    id=request.GET.get('id')
    menu = GlobalMenu.objects.get(pk=1)
    menu.item_set.filter(id=id).delete()
    return  HttpResponseRedirect(reverse('menuinfo'))