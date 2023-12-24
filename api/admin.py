from django.contrib import admin
from .models import Category, Product,Inquiry
from import_export.admin import ExportActionMixin

# Register your models here.
class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','categoryName', 'categoryLink')
    search_fields = ['id','categoryName', 'categoryLink']

class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','productName', 'category','productLink','packing','crop','listdes','isLive','isLatest','isHot')
    search_fields = ['id','productName', 'category','productLink','packing','crop','listdes','isLive','isLatest','isHot']
    list_filter = ['isLive',]    

class InquiryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName','contectno','email','selected_product','selected_category','description')
    search_fields = ['id','firstName', 'lastName','contectno','email','selected_product','selected_category','description']    
    list_filter = ['email','contectno']  

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Inquiry, InquiryAdmin)    