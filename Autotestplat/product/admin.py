# -*- coding:utf-8 -*-

from django.contrib import admin

# Register your models here.
from apitest.models import Apitest,Apis
from apptest.models import Appcase
from webtest.models import Webcase
from product.models import Product

from apitest.admin import ApitestAdmin

class ApitestAdmin(admin.TabularInline):
    list_display = ['apitestname', 'apitester','apitestresult','create_time','id','product']
    model = Apitest
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [ApitestAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [ApisAdmin]

class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename', 'apptestresult','create_time','id','product']
    model = Appcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [AppcaseAdmin]

class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult','create_time','id','product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','producter','create_time','id']
    inlines = [WebcaseAdmin]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','producter','create_time','id']   #��̨��ʾ��Ʒģ��

admin.site.register(Product,ProductAdmin)

