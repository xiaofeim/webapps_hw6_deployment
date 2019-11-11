from django.shortcuts import render,HttpResponse,reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Customer,Manager, Employee
from .forms import UserForm,RegisterForm
from django.contrib.auth import logout,authenticate,login
 

# The role of any new registered user will be customer.
# Only the manager can change the user's role.
# Any role changes will be applied after the current seesion expired.
def register(request):
    if request.method == 'GET':
        form_obj = RegisterForm()
        return render(request,'user_register.html',{'form_obj':form_obj})
    elif request.method == 'POST':
        form_obj = RegisterForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data['username']
            first_name = form_obj.cleaned_data['first_name']
            last_name = form_obj.cleaned_data['last_name']
            password = form_obj.cleaned_data['password']
            same_name_user = User.objects.filter(username=username)
            # If the username exists, then remaind the user to change another username.
            if same_name_user :
                error_msg = "Please choose another username !"
                return render(request, 'user_register.html', {'form_obj':form_obj,'error_msg':error_msg})
            else:
                # Create a new user.
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                Customer.objects.create(customer=user,c_name = username)
                request.session['customer'] = True
            return HttpResponseRedirect(reverse('dashboard'))

def user_login(request):
    if request.method == 'GET':
        form_obj = UserForm()
        return render(request,'user_login.html',{'form_obj':form_obj})
    elif request.method == "POST":
        form_obj = UserForm(request.POST)
        customer_list = Customer.objects.all()
        manager_list = Manager.objects.all()
        employee_list = Employee.objects.all()
        if form_obj.is_valid():
            username = form_obj.cleaned_data['username']
            password = form_obj.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                for c in customer_list:
                    if c.customer.username == username:
                        request.session['customer'] = True
                for m in manager_list:
                    if m.manager.username == username:
                        request.session['manager'] = True
                for e in employee_list:
                    if e.employee.username == username:
                        request.session['employee'] = True
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                error_msg = "User Name or Password is wrong!"
                return render(request,'user_login.html',{'error_msg':error_msg,'form_obj':form_obj})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dashboard'))