from django.contrib import admin
from .models import Order, Products

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Kermanshah Shopping"
admin.site.index_title = "Manage Kermanshah Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category', 'image_tag')
    search_fields = ('title', 'category')
    list_editable = ('price', 'discount_price')

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)