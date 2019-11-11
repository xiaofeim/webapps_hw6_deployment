from django.contrib import admin

from .models import GlobalMenu, Item

class ItemAdmin(admin.ModelAdmin):

    list_display = ('item_name', 'item_description', 'item_price','item_img')


admin.site.register(GlobalMenu)
admin.site.register(Item,ItemAdmin)
