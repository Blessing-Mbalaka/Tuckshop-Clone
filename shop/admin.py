from django.contrib import admin
from .models import Category, Product, Order, LineItem

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


class LineItemInline(admin.TabularInline):
    model = LineItem
    extra = 0
    readonly_fields = ['subtotal']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock_quantity', 'is_low_stock', 'is_active']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock_quantity', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description', 'image')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock_quantity', 'low_stock_threshold')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['reference', 'user', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['reference', 'user__username', 'user__email']
    readonly_fields = ['reference', 'total_amount', 'created_at', 'updated_at']
    inlines = [LineItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('reference', 'user', 'status')
        }),
        ('Financial', {
            'fields': ('total_amount',)
        }),
        ('Additional', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'subtotal']
    list_filter = ['order__status']
    search_fields = ['order__reference', 'product__name']
