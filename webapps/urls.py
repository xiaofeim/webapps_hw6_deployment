from django.contrib import admin
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.conf import settings
from manageItems import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.open_dashboard,name='dashboard'),
    url(r'^handle_qty$', views.handle_qty),
    url(r'^create_cart$', views.create_cart),
    url(r'^update_orders$', views.update_orders),
    url(r'^remove_from_cart$', views.remove_from_cart),
    url(r'^get_cart$', views.get_cart),
    url(r'^get_res$', views.get_res),
    
    path('login/', include('manageUsers.urls')),

    # Open the create, edit, and delete the cart item page.
    path('placeAnOrder/', include('addtocart.urls')),

    # Open the create, edit, and delete the menu item page.
    path('manageItems/', include('manageItems.urls')),

    # Open the create, edit, and delete the restaurant page.
    path('manageStores/', include('manageStores.urls')),

    # Open the create, edit, and delete the manager page.
    path('manageManager/', include('manageMags.urls')),

    # Open the create, edit, and delete the employee page.
    path('manageEmployee/', include('manageEmps.urls')),

    # Open the create, edit, and delete the submitted orders page.
    path('manageOrders/', include('manageOrders.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
