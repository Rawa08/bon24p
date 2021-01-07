from django.contrib import admin
from .models import Customer, ProductList
from product.models import Product

class ProductListAdmin(admin.StackedInline):
    model = ProductList
    raw_id_fields= ('products', 'orderBy')
    

    
        
         

class CustomerAdmin(admin.ModelAdmin):
    inlines = (ProductListAdmin,)

    
    list_display = ['id','name', 'phone','email', 'city','handeld','deliverd','paid', 'date']
    search_fields = ('name', 'phone', 'email', 'city','handeld','deliverd','paid')
    list_editable = ('handeld','deliverd','paid')
    actions = ['paid', 'deliverd', 'handeld']
    
    def paid(self, request, queryset):
        queryset.update(paid=True)
    def deliverd(self, request, queryset):
        queryset.update(deliverd=True)    
    def handeld(self, request, queryset):
        queryset.update(handeld=True)   

admin.site.register(Customer, CustomerAdmin)    
