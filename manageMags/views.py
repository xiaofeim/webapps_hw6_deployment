from django.shortcuts import render,HttpResponse,reverse
from django.http import HttpResponseRedirect
from manageItems.models import GlobalMenu,Item
from manageStores.models import Restaurant
from manageUsers.models import Customer,Employee,Manager
from django.contrib.auth.models import User
from manageMags.forms import ManagerForm, MRelationForm

def view_all_managers(request):
    if request.method=='GET':
        m = Manager.objects.all()
        store_list = Restaurant.objects.all()
        context = {
            'manager_list': m,
        }
        return render(request, 'view_all_managers.html', context)

def add_manager(request):
    if request.method=='GET':
        form_obj = ManagerForm()
        store_list = Restaurant.objects.all()
        employee_list = Employee.objects.all()
        return render(request, 'add_manager.html',{'form_obj':form_obj,'employee_list':employee_list})
    elif request.method=='POST':
        form_obj = ManagerForm(request.POST)
        if form_obj.is_valid():
            m_name = form_obj.cleaned_data['m_name']
            employee_list = Employee.objects.all()
            for e in employee_list:
                if e.employee.username == m_name:
                    user = e.employee
                    eID = e.id
                    obj = Manager.objects.create(manager=user,m_name=m_name)
                    Employee.objects.get(id=eID).delete()
            store_list = form_obj.cleaned_data.get("restaurant")
            obj.restaurant.add(*store_list)
            obj.save()
            return HttpResponseRedirect(reverse('managerinfo'))
        else:
            error_msg = "You should select at least one Working Location!"
            employee_list = Employee.objects.all()
            return render(request, 'add_manager.html',{'form_obj':form_obj,'employee_list':employee_list,'error_msg':error_msg})


def delete_manager(request):
    m_id = request.GET.get('id')
    m = Manager.objects.get(id=m_id)
    # If the manager is deleted, this username will only have customer's permission.
    user = m.manager
    obj = Customer.objects.create(customer=user)
    m.restaurant.clear()
    m.delete()
    return HttpResponseRedirect(reverse('managerinfo'))

# Manage the relationship between manager and restaurant.
def add_store_manager(request):
    if request.method=='GET':
        select_list = []
        m_id = request.GET.get('id')
        m = Manager.objects.get(pk=m_id)

        store_list = Restaurant.objects.all()
        work_list = m.restaurant.all()
        for w in store_list:
            if w in work_list:
                pass
            else:
                select_list.append(w)
        return render(request, 'add_store_mag.html',{'m': m,'store_list': select_list})
    elif request.method=='POST':
        m_id = request.GET.get('id')
        m = Manager.objects.get(pk=m_id)
        store_list = request.POST.getlist('res')
        m.restaurant.add(*store_list)
        m.save()
        return HttpResponseRedirect(reverse('managerinfo'))

def remove_store_manager(request):
    if request.method=='GET':
        m_id = request.GET.get('id')
        m = Manager.objects.get(pk=m_id)
        store_list = Restaurant.objects.all()
        context = {
            'm': m,
            'store_list': store_list,
        }
        return render(request, 'remove_store_mag.html',context)
    elif request.method=='POST':
        m_id = request.GET.get('id')
        m = Manager.objects.get(pk=m_id)
        store_list = request.POST.getlist('res')
        m.restaurant.remove(*store_list)
        return HttpResponseRedirect(reverse('managerinfo'))
