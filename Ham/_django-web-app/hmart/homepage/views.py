from django.shortcuts import render, HttpResponse
from homepage.models import *
from django.views.generic import TemplateView
from django.db import models
from django.views.generic import ListView

import MySQLdb

# Create your views here.
def index(request):
    #return HttpResponse('안녕하세요 한아름 마트십니다' )
    return render(request, 'homepage/index.html')


class StoreList(ListView):
    model = Store
    context_oject_name = 'hmarts'
    template_name = 'homepage/stores.html'
    queryset = Store
    # queryset = Store.objects.raw(
    #     """
    #     Select storeState,ID From store where storestate = 'Georgia'
    #     """)

class ProductList(ListView):
    model = Product
    context_oject_name = 'products'
    template_name = 'homepage/products.html'

    queryset = Product.objects.raw(
        """
        Select ID, productname From product where productdescription = 'South Korea'
        """)


class SalesList(ListView):
    model = Sales
    context_object_name = 'sales'
    template_name = 'homepage/sales.html'
    queryset = Sales.objects.order_by('store')
    
    
    

# def queryTest(request):
    
#     x = list( Sales.objects.all())
#     return render(request, 'homepage/sales.html', {'queryset': x})


# def queryTest1(request):
    
#     store_stores = list(Store.objects.all().sales_set.all())
#     return render(request, 'homepage/storeSales.html', {'storeSales': store_sales})
