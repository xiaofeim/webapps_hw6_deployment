from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from manageItems.models import GlobalMenu, Item
from .models import Restaurant
from django import forms
from .forms import RestaurantForm


def view_all_stores(request):
    if request.method == "GET":
        store_list = Restaurant.objects.all().order_by("id")
        context = {"store_list": store_list}
        return render(request, "view_all_stores.html", context)


def add_store(request):
    if request.method == "POST":
        form_obj = RestaurantForm(request.POST)
        if form_obj.is_valid():
            global_menu = form_obj.cleaned_data.get("global_menu")
            location = form_obj.cleaned_data.get("restauran_location")
            r = Restaurant(global_menu=global_menu, restauran_location=location)
            r.save()
            return HttpResponseRedirect(reverse("storeinfo"))
    elif request.method == "GET":
        form_obj = RestaurantForm()
        return render(request, "add_store.html", {"form_obj": form_obj})


def edit_store(request):
    if request.method == "GET":
        store_id = request.GET.get("id")
        store = Restaurant.objects.get(id=store_id)
        form_obj = RestaurantForm(instance=store)
        return render(
            request, "edit_store.html", {"form_obj": form_obj, "store": store}
        )
    elif request.method == "POST":
        store_id = request.GET.get("id")
        store = Restaurant.objects.get(id=store_id)
        form_obj = RestaurantForm(request.POST, instance=store)
        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect(reverse("storeinfo"))


def delete_store(request):
    store_id = request.GET.get("id")
    store = Restaurant.objects.get(id=store_id)
    store.delete()
    return HttpResponseRedirect(reverse("storeinfo"))

