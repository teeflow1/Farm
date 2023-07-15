from django.contrib import admin
from farm_app.models import Category, Farmer, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address

class ProductImageAdmin(admin. TabularInline):
    model = ProductImage
    
class ProductAdmin(admin. ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user', 'title', 'product_images', 'price', 'featured', 'product_status']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
    
class FarmerAdmin(admin.ModelAdmin):
    list_display=['title', 'farmer_image', 'description']
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date',  'product_status']
    
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'price', 'images', 'item', 'total', 'Qty', ]
    
    
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']
    
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status' ]
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)

'''
admin.site.register(Farmer)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CartOrder)
admin.site.register(CartOrderItem)
admin.site.register(ProductView)
admin.site.register(wishlist)
admin.site.register(Address)
'''
