from django.contrib import admin

from product.models import Product, ProductAccess


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    pass
