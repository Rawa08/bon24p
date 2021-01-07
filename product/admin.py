from django.contrib import admin
from .models import Brand, Product
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from decimal import Decimal
from.views import save_image
# Register your models here.

#admin = db_admin 7-2
#class PriceInline(admin.StackedInline):
#    model = Pricing


#for import settings
##working

class ProductResorce(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        Brand.objects.get_or_create(
            name=row.get('BRAND')
        )
        
    
        


    ean = fields.Field(column_name='EAN',
                         attribute='id')
    brand_name1 = fields.Field(column_name='BRAND',
                         attribute='brand_name',
                         widget=ForeignKeyWidget(Brand,'name'))
    name = fields.Field(column_name='NAME',
                         attribute='name')
    
    sex = fields.Field(column_name='SEX',
                           attribute='sex')
    p_type = fields.Field(column_name='TYPE',
                          attribute='p_type')
    image_link = fields.Field(column_name='PICTURE',
                          attribute='image_link')
    stock_price = fields.Field(column_name='PRICE (EUR)',
                          attribute='stock_price')      
    volume = fields.Field(column_name='SIZE',
                          attribute='volume')                                                      


   

    class Meta:
       
        model = Product
        #exclude = ('id','show','in_stock','created')
        import_id_fields = ('ean',)
        
        fields=['id','brand_name1' ,'name', 'sex', 'p_type','image_link','stock_price','volume']
        export_order = ['id','brand_name1','name', 'sex', 'p_type','image_link','stock_price',]
        #export_order = ('name', 'Brand__BrandName', 'gender', 'stockPrice')
        
        



        
#showing in product add
class ProductImportAdmin(ImportExportModelAdmin):

    
    list_display = ('name','brand_name','score','sex', 'show','in_stock','volume','p_type','price','stock_price')
    list_editable = ('in_stock', 'show','price','stock_price','score',)
    search_fields = ('name', 'sex', 'p_type', 'id', 'brand_name__name')
    resource_class = ProductResorce
    #fields = ['name', 'gender', 'Brand', 'author',  'stockPrice', 'description']
    actions = ['showEnable','showDisable','inStockEnable','inStockDisable','scoreZero','scoreUpp','scoreDown','priceFix', 'save_image']

    def showEnable(self, request, queryset):
        queryset.update(show=True)
    def showDisable(self, request, queryset):
        queryset.update(show=False)    
    def inStockEnable(self, request, queryset):
        queryset.update(in_stock=True)  
    def inStockDisable(self, request, queryset):
        queryset.update(in_stock=False)
       
    def scoreUpp(self, request, queryset):
        objectP = queryset
        for p in objectP:
            p.score = p.score +1
            p.save()
        
    
    def scoreDown(self, request, queryset):
        objectP = queryset
        for p in objectP:
            p.score = p.score -1
            p.save()
           
    def priceFix(self, request, queryset):
        objectP = queryset
        for p in objectP:
            p.price = (p.stock_price*Decimal(1.3))*Decimal(1.3)
        
            p.save()
             
    def scoreZero(self, request, queryset):
        objectP = queryset
        for p in objectP:
            p.score = 0
            p.save()     

             
     
            

  
    
class BrandOrderInline(admin.StackedInline):
    model = Product


class BrandAdmin(admin.ModelAdmin):
    inlines = (BrandOrderInline, )
    list_display = ('name',)
    
    search_fields = ('name',)
    





admin.site.register(Product, ProductImportAdmin)
admin.site.register(Brand,BrandAdmin)


