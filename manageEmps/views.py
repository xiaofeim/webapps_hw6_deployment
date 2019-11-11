from django.shortcuts import render, HttpResponse, reverse
from django.http import HttpResponseRedirect
from manageItems.models import GlobalMenu, Item
from manageStores.models import Restaurant
from manageUsers.models import Customer, Employee, Manager
from django.contrib.auth.models import User
from manageEmps.forms import EmployeeForm, ERelationForm


def view_all_employees(request):
    if request.method == 'GET':
        e = Employee.objects.all().order_by('id')
        store_list = Restaurant.objects.all().order_by('id')
        context = {
            'employee_list': e,
        }
        return render(request, 'view_all_emps.html', context)


def add_employee(request):
    if request.method == 'GET':
        form_obj = EmployeeForm()
        customer_list = Customer.objects.all()
        return render(request, 'add_employee.html', {'form_obj': form_obj, 'customer_list': customer_list})
    elif request.method == 'POST':
        form_obj = EmployeeForm(request.POST)
        if form_obj.is_valid():
            e_name = form_obj.cleaned_data.get("e_name")
            # Find the customer whose username equals to employee name.
            # Change the customer role to employee role.
            # Maintain the user object in the user models, but delete the customer object from Customer Model.
            customer_list = Customer.objects.all()
            for c in customer_list:
                if c.customer.username == e_name:
                    user = c.customer
                    customerID = c.id
                    obj = Employee.objects.create(employee=user, e_name=e_name)
                    Customer.objects.get(id=customerID).delete()
            store_list = form_obj.cleaned_data.get("restaurant")
            obj.restaurant.add(*store_list)
            obj.save()
            return HttpResponseRedirect(reverse('employeeinfo'))
        else:
            error_msg = "You should select at least one Working Location!"
            customer_list = Customer.objects.all()
            return render(request, 'add_employee.html', {'form_obj': form_obj, 'customer_list': customer_list, 'error_msg': error_msg})


def delete_employee(request):
    e_id = request.GET.get('id')
    e = Employee.objects.get(id=e_id)
    # If the employee is deleted, this username will only have customer's permission.
    user = e.employee
    obj = Customer.objects.create(customer=user)
    e.restaurant.clear()
    e.delete()
    return HttpResponseRedirect(reverse('employeeinfo'))

# Manage the relationship between employee and restaurant.
def add_store_employee(request):
    if request.method == 'GET':
        # The restaurant location that can be chosen by manager.
        select_list = []
        e_id = request.GET.get('id')
        e = Employee.objects.get(pk=e_id)
        # All the restaurant location.
        store_list = Restaurant.objects.all()
        # The specific employee's working location.
        work_list = e.restaurant.all()
        for w in store_list:
            if w in work_list:
                pass
            else:
                select_list.append(w)
        return render(request, 'edit_employee.html', {'e': e, 'store_list': select_list, })
    elif request.method == 'POST':
        e_id = request.GET.get('id')
        e = Employee.objects.get(pk=e_id)
        work_list = request.POST.getlist('res')
        e.restaurant.add(*work_list)
        e.save()
        return HttpResponseRedirect(reverse('employeeinfo'))


def remove_store_employee(request):
    if request.method == 'GET':
        e_id = request.GET.get('id')
        e = Employee.objects.get(pk=e_id)
        store_list = Restaurant.objects.all()
        context = {
            'e': e,
            'store_list': store_list,
        }
        return render(request, 'remove_store_emp.html', context)
    elif request.method == 'POST':
        e_id = request.GET.get('id')
        e = Employee.objects.get(pk=e_id)
        store_list = request.POST.getlist('res')
        e.restaurant.remove(*store_list)
        return HttpResponseRedirect(reverse('employeeinfo'))
